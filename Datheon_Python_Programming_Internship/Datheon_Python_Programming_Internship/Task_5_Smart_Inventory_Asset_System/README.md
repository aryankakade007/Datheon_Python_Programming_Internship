# Enterprise Smart Inventory & Asset System

## About the Project

The Enterprise Smart Inventory & Asset System is a Python-based console application developed as part of the **Datheon Python Programming Internship**.

The project demonstrates Object-Oriented Programming (OOP) concepts by managing different types of inventory items, including Books, Magazines, and Digital Media.

It allows users to add items, view inventory, borrow and return items, calculate late fees, and maintain an activity audit report.

## Features

- Add Books, Magazines, and Digital Media.
- Display inventory in a formatted table.
- Borrow and return inventory items.
- Calculate late fees based on item type.
- Display detailed information about individual items.
- Maintain an inventory activity audit report.
- Track the total number of inventory items.
- Validate user input and handle errors.

## OOP Concepts Implemented

1. **Classes and Objects:** Created classes for Item, Book, Magazine, DigitalMedia, and InventoryManager.
2. **Inheritance:** Book, Magazine, and DigitalMedia inherit from the abstract Item class.
3. **Abstraction:** Used Python's `abc` module and abstract methods.
4. **Encapsulation:** Used private attributes such as `__price` and `__borrow_date`.
5. **Polymorphism:** Implemented different late-fee calculations for different item types.
6. **Method Overriding:** Derived classes provide their own implementations of abstract methods.
7. **Properties:** Used `@property` and setters for controlled attribute access and validation.
8. **Magic Methods:** Implemented `__str__`, `__repr__`, `__len__`, and `__eq__`.

## Project Structure

```text
Task_5_Smart_Inventory_Asset_System/
│
├── models.py
├── inventory.py
├── main.py
├── test_oop.py
└── README.md
```

## Technologies Used

- Python 3
- Object-Oriented Programming
- Python ABC Module
- Python DateTime Module

## How to Run the Project

### 1. Clone or download the repository

### 2. Open the project folder in VS Code.

### 3. Run the main application

```bash
python main.py
```

### 4. Run the OOP concept tests

```bash
python test_oop.py
```

## Application Menu

```text
SMART INVENTORY & ASSET SYSTEM

1. Add New Item
2. View Inventory
3. Checkout / Borrow Item
4. Return Item
5. View Item Details
6. View Audit Report
7. Total Inventory Count
8. Exit
```

## Testing

The project includes a separate test script, `test_oop.py`, to demonstrate and verify the implementation of the major OOP concepts.

The tests cover:
- Object creation and inheritance.
- Abstract class restrictions.
- Polymorphism and method overriding.
- Encapsulation and price validation.
- Magic methods.

All demonstrated OOP tests execute successfully.

## Internship Information

**Organization:** Datheon – AI Systems & Automation Studio

**Program:** Python Programming Internship

**Project:** Task 5 – OOP Architecture: Enterprise Smart Inventory & Asset System

---

Developed by **Janhvi Dalavi**