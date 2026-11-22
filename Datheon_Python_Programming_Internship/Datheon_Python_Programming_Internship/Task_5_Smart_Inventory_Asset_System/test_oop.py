
from models import Item, Book, Magazine, DigitalMedia


print("\n========== OOP CONCEPT TESTING ==========")

# 1. Classes and Objects
book = Book("B201", "Python Basics", 400, "John", 300)
magazine = Magazine("M201", "Tech World", 150, "10", "Tech Pub")
digital = DigitalMedia("D201", "Python Course", 250, "MP4", 500)

print("\n1. Classes and Objects")
print(book)
print(magazine)
print(digital)

# 2. Inheritance
print("\n2. Inheritance")
print("Book is an Item:", isinstance(book, Item))
print("Magazine is an Item:", isinstance(magazine, Item))
print("DigitalMedia is an Item:", isinstance(digital, Item))

# 3. Abstraction
print("\n3. Abstraction")
try:
    item = Item("I201", "Test Item", 100)
except TypeError:
    print("Abstract class cannot be instantiated.")

# 4. Polymorphism and Method Overriding
print("\n4. Polymorphism")
items = [book, magazine, digital]

for item in items:
    print(item.title, "Late Fee:", item.calculate_fee(10))
    print(item.display_metadata())

# 5. Encapsulation and Properties
print("\n5. Encapsulation and Properties")
print("Original Book Price:", book.price)

book.price = 500
print("Updated Book Price:", book.price)

try:
    book.price = -100
except ValueError as error:
    print("Validation Working:", error)

# 6. Magic Methods
print("\n6. Magic Methods")

print("__str__:", str(book))
print("__repr__:", repr(book))
print("__len__:", len(book))

another_book = Book("B201", "Another Title", 300, "David", 200)
print("__eq__:", book == another_book)

print("\n========== ALL OOP TESTS COMPLETED ==========")
