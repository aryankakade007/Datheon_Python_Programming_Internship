from datetime import date
from models import Item


class InventoryManager:
    """Manages inventory items, borrowing, and returns."""

    def __init__(self):
        self.items = {}
        self.audit_log = []

    def add_item(self, item):
        if not isinstance(item, Item):
            raise TypeError("Only valid inventory items can be added.")

        if item.item_id in self.items:
            raise ValueError("An item with this ID already exists.")

        self.items[item.item_id] = item
        self.audit_log.append(
            f"{date.today()} - Added: {item.title}"
        )
        print("Item added successfully!")

    def checkout_item(self, item_id):
        item = self.items.get(item_id)

        if item is None:
            print("Item not found.")
            return

        if item.borrow_date is not None:
            print("This item is already borrowed.")
            return

        item.borrow_date = date.today()

        self.audit_log.append(
            f"{date.today()} - Borrowed: {item.title}"
        )

        print(f"'{item.title}' borrowed successfully!")

    def return_item(self, item_id):
        item = self.items.get(item_id)

        if item is None:
            print("Item not found.")
            return

        if item.borrow_date is None:
            print("This item is not currently borrowed.")
            return

        borrow_date = item.borrow_date
        days = (date.today() - borrow_date).days

        fee = item.calculate_fee(days)

        item.borrow_date = None

        self.audit_log.append(
            f"{date.today()} - Returned: {item.title}"
        )

        print(f"'{item.title}' returned successfully!")
        print(f"Borrowed for: {days} days")
        print(f"Late fee: Rs. {fee}")

    def display_inventory(self):
        if not self.items:
            print("\nInventory is empty.")
            return

        print("\n" + "=" * 85)
        print("                    INVENTORY REPORT")
        print("=" * 85)

        print(
            f"{'ID':<10}{'Title':<25}{'Type':<18}"
            f"{'Price':<12}{'Status':<15}"
        )
        print("-" * 85)

        for item in self.items.values():
            item_type = item.__class__.__name__

            status = (
                "Borrowed"
                if item.borrow_date is not None
                else "Available"
            )

            print(
                f"{item.item_id:<10}"
                f"{item.title[:23]:<25}"
                f"{item_type:<18}"
                f"Rs.{item.price:<9.2f}"
                f"{status:<15}"
            )

        print("=" * 85)
        print(f"Total items: {len(self)}")

   
    def display_audit_report(self):
        print("\n" + "=" * 75)
        print("                         INVENTORY AUDIT REPORT")
        print("=" * 75)

        if not self.audit_log:
            print("No activities recorded yet.")
            return

        print(f"{'No.':<8}{'Date':<18}{'Activity'}")
        print("-" * 75)

        for number, record in enumerate(self.audit_log, start=1):
            parts = record.split(" - ", 1)

            activity_date = parts[0]
            activity = parts[1] if len(parts) > 1 else record

            print(f"{number:<8}{activity_date:<18}{activity}")

        print("=" * 75)
        print(f"Total activities: {len(self.audit_log)}")


    def __len__(self):
        return len(self.items)