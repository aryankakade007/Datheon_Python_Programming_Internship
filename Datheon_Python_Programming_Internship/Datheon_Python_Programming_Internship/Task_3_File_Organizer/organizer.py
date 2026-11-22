
import os
import shutil
from datetime import datetime

# File categories and their extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".c", ".html", ".css", ".js"],
}

LOG_FILE = "organizer_log.txt"


def get_category(extension):
    """Return the category for a file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def get_unique_path(destination):
    """Avoid overwriting files with the same name."""
    if not os.path.exists(destination):
        return destination

    folder = os.path.dirname(destination)
    filename = os.path.basename(destination)
    name, extension = os.path.splitext(filename)

    counter = 1
    while True:
        new_name = f"{name}_{counter}{extension}"
        new_path = os.path.join(folder, new_name)

        if not os.path.exists(new_path):
            return new_path

        counter += 1


def write_log(message):
    """Write an entry to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}\n")


def organize_files(directory):
    """Organize files in the selected directory."""
    if not os.path.isdir(directory):
        print("Error: The directory does not exist.")
        return

    moved_count = 0
    skipped_count = 0
    error_count = 0
    category_counts = {}

    print("\nOrganizing files...\n")

    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if not entry.is_file():
                    continue

                filename = entry.name
                extension = os.path.splitext(filename)[1].lower()
                category = get_category(extension)

                destination_folder = os.path.join(directory, category)

                try:
                    os.makedirs(destination_folder, exist_ok=True)

                    source_path = entry.path
                    destination_path = os.path.join(
                        destination_folder, filename
                    )
                    destination_path = get_unique_path(destination_path)

                    shutil.move(source_path, destination_path)

                    moved_count += 1
                    category_counts[category] = (
                        category_counts.get(category, 0) + 1
                    )

                    message = f"Moved {filename} to {category}"
                    print(f"[OK] {message}")
                    write_log(message)

                except PermissionError:
                    error_count += 1
                    print(f"[ERROR] Permission denied: {filename}")
                    write_log(f"Permission denied: {filename}")

                except OSError as error:
                    error_count += 1
                    print(f"[ERROR] Could not move {filename}: {error}")
                    write_log(f"Error moving {filename}: {error}")

    except PermissionError:
        print("Error: Permission denied while accessing the directory.")
        return

    print("\n" + "=" * 40)
    print("       FILE ORGANIZATION SUMMARY")
    print("=" * 40)
    print(f"Files organized : {moved_count}")
    print(f"Files skipped   : {skipped_count}")
    print(f"Errors          : {error_count}")

    if category_counts:
        print("\nFiles by category:")
        for category, count in sorted(category_counts.items()):
            print(f"  {category:<12}: {count}")

    print("=" * 40)
    write_log(
        f"Completed. Moved: {moved_count}, "
        f"Skipped: {skipped_count}, Errors: {error_count}"
    )


def main():
    print("=" * 40)
    print("   AUTOMATED FILE ORGANIZER")
    print("=" * 40)
    print("Organizes files into folders by category.")
    print("Files are moved, not deleted.\n")

    directory = input(
        "Enter the directory path to organize: "
    ).strip().strip('"')

    if not directory:
        print("Error: Directory path cannot be empty.")
        return

    print(f"\nSelected directory: {directory}")
    confirm = input("Continue? (y/n): ").strip().lower()

    if confirm == "y":
        organize_files(directory)
    else:
        print("Operation cancelled. No files were moved.")


if __name__ == "__main__":
    main()
