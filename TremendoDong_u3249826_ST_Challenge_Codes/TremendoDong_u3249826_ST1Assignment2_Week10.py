# TremendoDong_u3249826_ST1Assignment2_Week10

import tkinter as tk
from tkinter import messagebox


# Library Item Class
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

# Book Class (extended from LibraryItem)
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


class BookViewGUI(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Library Information System")


        self.lbl_item_name = tk.Label(self, text="Item Name:")
        self.lbl_item_name.grid(row=0, column=0)
        self.entry_item_name = tk.Entry(self)
        self.entry_item_name.grid(row=0, column=1)

        self.lbl_author = tk.Label(self, text="Author:")
        self.lbl_author.grid(row=1, column=0)
        self.entry_author = tk.Entry(self)
        self.entry_author.grid(row=1, column=1)

        self.lbl_publisher = tk.Label(self, text="Publisher:")
        self.lbl_publisher.grid(row=2, column=0)
        self.entry_publisher = tk.Entry(self)
        self.entry_publisher.grid(row=2, column=1)

        self.lbl_num_pages = tk.Label(self, text="Number of Pages:")
        self.lbl_num_pages.grid(row=3, column=0)
        self.entry_num_pages = tk.Entry(self)
        self.entry_num_pages.grid(row=3, column=1)

        self.lbl_has_ebook = tk.Label(self, text="Has eBook (True/False):")
        self.lbl_has_ebook.grid(row=4, column=0)
        self.entry_has_ebook = tk.Entry(self)
        self.entry_has_ebook.grid(row=4, column=1)

        self.btn_submit = tk.Button(self, text="Submit", command=self.create_book)
        self.btn_submit.grid(row=5, column=0, columnspan=2)

    def create_book(self):
        try:
            item_name = self.entry_item_name.get()
            author = self.entry_author.get()
            publisher = self.entry_publisher.get()
            num_pages = int(self.entry_num_pages.get())
            has_ebook = self.entry_has_ebook.get().lower() == 'true'

            book = Book(item_name, author, publisher, num_pages, has_ebook)
            messagebox.showinfo("Success", f"Created Book: {book}")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = BookViewGUI()
    app.mainloop()