Automated File Organizer & Cleanup Utility
About the Project
The Automated File Organizer is a Python-based utility developed as part of the Datheon Python Programming Internship.

It automates file organization by sorting files into category-based folders according to their extensions. The utility uses Python's built-in os and shutil libraries to perform filesystem operations safely and efficiently.

Features
Organizes files by extension and category.
Automatically creates category folders.
Supports documents, images, videos, audio, archives, code, and other files.
Prevents overwriting by renaming duplicate files.
Handles invalid directory paths and filesystem errors.
Displays a summary of organized files.
Maintains a timestamped log of file operations.
Includes confirmation before moving files.
Technologies Used
Python 3
os
shutil
datetime
Project Structure
Task_3_File_Organizer/
├── organizer.py
├── README.md
└── organizer_log.txt  (generated when the program runs)
How to Run
Install Python 3.
Open the project folder in VS Code.
Open the terminal in the project directory.
Run the following command:
python organizer.py
Enter the directory path you want to organize.
Confirm the operation when prompted.
Example
Before organizing:

sample_folder/
├── notes.txt
├── photo.jpg
├── video.mp4
├── project.py
└── archive.zip
After organizing:

sample_folder/
├── Documents/
│   └── notes.txt
├── Images/
│   └── photo.jpg
├── Videos/
│   └── video.mp4
├── Code/
│   └── project.py
└── Archives/
    └── archive.zip
Safety
The utility moves files into category folders and does not intentionally delete them. Duplicate filenames are renamed to prevent overwriting existing files.

Always test the utility on a sample folder before organizing important directories.

Internship Task
Task 3: Automated File Organizer & Cleanup Utility

Organization: Datheon — AI Systems & Automation Studio

Program: Python Programming Internship