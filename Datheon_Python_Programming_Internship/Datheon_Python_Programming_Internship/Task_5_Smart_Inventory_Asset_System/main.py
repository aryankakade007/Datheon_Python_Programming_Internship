from models import Book, Magazine, DigitalMedia
from inventory import InventoryManager


def add_new_item(inventory):
    print("\n--- ADD NEW ITEM ---")
    print("1. Book")
    print("2. Magazine")
    print("3. Digital Media")

    choice = input("Select item type: ").strip()

    try:
        item_id = input("Enter Item ID: ").strip()
        if not item_id:
            print("Item ID cannot be empty.")
            return

        title = input("Enter title: ").strip()
        if not title:
            print("Title cannot be empty.")
            return

        price = float(input("Enter price (Rs.): "))

        if choice == "1":
            author = input("Enter author: ").strip()
            pages = int(input("Enter number of pages: "))

            if not author or pages <= 0:
                print("Please enter valid author and page details.")
                return

            item = Book(item_id, title, price, author, pages)

        elif choice == "2":
            issue = input("Enter issue number: ").strip()
            publisher = input("Enter publisher: ").strip()

            if not issue or not publisher:
                print("Issue number and publisher are required.")
                return

            item = Magazine(
                item_id, title, price, issue, publisher
            )

        elif choice == "3":
            file_format = input("Enter file format: ").strip()
            file_size = float(input("Enter file size (MB): "))

            if not file_format or file_size <= 0:
                print("Please enter valid digital media details.")
                return

            item = DigitalMedia(
                item_id, title, price, file_format, file_size
            )

        else:
            print("Invalid item type.")
            return

        inventory.add_item(item)

    except ValueError as error:
        print(f"Invalid input: {error}")

    except (TypeError, KeyError) as error:
        print(f"Error: {error}")


def display_item_details(inventory):
    item_id = input("Enter Item ID: ").strip()
    item = inventory.items.get(item_id)

    if item is None:
        print("Item not found.")
        return

    print("\n--- ITEM DETAILS ---")
    print(f"Item: {item}")
    print(f"Type: {item.__class__.__name__}")
    print(f"Price: Rs. {item.price:.2f}")
    print(f"Details: {item.display_metadata()}")
    print(f"Borrow Date: {item.borrow_date}")


def main():
    inventory = InventoryManager()

    # Sample inventory items
    sample_items = [
        Book("B101", "Python Programming", 450, "John Smith", 350),
        Magazine("M101", "Tech Today", 120, "15", "Tech Publications"),
        DigitalMedia("D101", "Python Tutorial", 299, "MP4", 500)
    ]

    for item in sample_items:
        inventory.add_item(item)

    while True:
        print("\n" + "=" * 45)
        print("       SMART INVENTORY & ASSET SYSTEM")
        print("=" * 45)
        print("1. Add New Item")
        print("2. View Inventory")
        print("3. Checkout / Borrow Item")
        print("4. Return Item")
        print("5. View Item Details")
        print("6. View Audit Report")
        print("7. Total Inventory Count")
        print("8. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_new_item(inventory)

        elif choice == "2":
            inventory.display_inventory()

        elif choice == "3":
            item_id = input("Enter Item ID to borrow: ").strip()
            inventory.checkout_item(item_id)

        elif choice == "4":
            item_id = input("Enter Item ID to return: ").strip()
            inventory.return_item(item_id)

        elif choice == "5":
            display_item_details(inventory)

        elif choice == "6":
            inventory.display_audit_report()

        elif choice == "7":
            print(f"\nTotal inventory items: {len(inventory)}")

        elif choice == "8":
            print("\nThank you for using Smart Inventory System!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()