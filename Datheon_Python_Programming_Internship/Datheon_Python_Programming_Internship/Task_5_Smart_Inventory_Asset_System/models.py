
from abc import ABC, abstractmethod
from datetime import date


class Item(ABC):
    """Abstract base class for inventory items."""

    def __init__(self, item_id, title, price):
        self.item_id = item_id
        self.title = title
        self.price = price
        self.__borrow_date = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero.")
        self.__price = value

    @property
    def borrow_date(self):
        return self.__borrow_date

    @borrow_date.setter
    def borrow_date(self, value):
        if value is not None and not isinstance(value, date):
            raise ValueError("Borrow date must be a date.")
        self.__borrow_date = value

    @abstractmethod
    def calculate_fee(self, days):
        pass

    @abstractmethod
    def display_metadata(self):
        pass

    def __str__(self):
        return f"{self.item_id} - {self.title}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.item_id!r}, {self.title!r})"

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.item_id == other.item_id
        return False


class Book(Item):
    """Represents a book in the inventory."""

    def __init__(self, item_id, title, price, author, pages):
        super().__init__(item_id, title, price)
        self.author = author
        self.pages = pages

    def calculate_fee(self, days):
        if days <= 7:
            return 0
        return (days - 7) * 2

    def display_metadata(self):
        return f"Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages


class Magazine(Item):
    """Represents a magazine in the inventory."""

    def __init__(self, item_id, title, price, issue_number, publisher):
        super().__init__(item_id, title, price)
        self.issue_number = issue_number
        self.publisher = publisher

    def calculate_fee(self, days):
        if days <= 3:
            return 0
        return (days - 3) * 1

    def display_metadata(self):
        return f"Issue: {self.issue_number}, Publisher: {self.publisher}"


class DigitalMedia(Item):
    """Represents digital media in the inventory."""

    def __init__(self, item_id, title, price, file_format, file_size):
        super().__init__(item_id, title, price)
        self.file_format = file_format
        self.file_size = file_size

    def calculate_fee(self, days):
        return 0

    def display_metadata(self):
        return f"Format: {self.file_format}, Size: {self.file_size} MB"
