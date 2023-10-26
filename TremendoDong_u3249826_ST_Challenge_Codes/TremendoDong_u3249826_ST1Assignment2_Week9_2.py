# TremendoDong_u3249826_ST1Assignment2_Week9_2

class Book(LibraryItem):
    def __init__(self, item_name, author, publisher, num_pages, has_ebook):
        super().__init__(item_name, author, publisher)
        self._num_pages = num_pages
        self._has_ebook = has_ebook


    def get_num_pages(self):
        return self._num_pages

    def has_ebook(self):
        return self._has_ebook

    # Mutator methods
    def set_num_pages(self, num_pages):
        self._num_pages = num_pages

    def set_has_ebook(self, has_ebook):
        self._has_ebook = has_ebook

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Number of Pages: {self._num_pages}, Has eBook: {self._has_ebook}"


if __name__ == "__main__":
    book1 = Book("Book D", "Author D", "Publisher D", 300, True)
    print(book1)
