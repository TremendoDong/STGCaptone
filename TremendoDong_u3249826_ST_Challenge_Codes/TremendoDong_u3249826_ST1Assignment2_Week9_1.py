# TremendoDong_u3249826_ST1Assignment2_Week9_1

class LibraryItem:
    def __init__(self, item_name, author, publisher):
        self._item_name = item_name
        self._author = author
        self._publisher = publisher

    # Accessor methods
    def get_item_name(self):
        return self._item_name

    def get_author(self):
        return self._author

    def get_publisher(self):
        return self._publisher

    # Mutator methods
    def set_item_name(self, item_name):
        self._item_name = item_name

    def set_author(self, author):
        self._author = author

    def set_publisher(self, publisher):
        self._publisher = publisher

    def __str__(self):
        return f"Item Name: {self._item_name}, Author: {self._author}, Publisher: {self._publisher}"


if __name__ == "__main__":
    item1 = LibraryItem("Book A", "Author A", "Publisher A")
    item2 = LibraryItem("Book B", "Author B", "Publisher B")
    item3 = LibraryItem("Book C", "Author C", "Publisher C")

    print(item1)
    print(item2)
    print(item3)


