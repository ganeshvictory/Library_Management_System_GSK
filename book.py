#All operations like adding, deleting, updating, searching and listing the books stored in our database is done in this book.py classes and methods

class Book:
    """
    Represents a book with basic attributes: title, author, ISBN, and quantity.
    """
    def __init__(self, title: str, author: str, isbn: str, qty: int = 0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.qty = qty

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Quantity: {self.qty}"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

class Books:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn, qty):
        new_book = Book(title, author, isbn, qty)
        if new_book in self.books:
            return "Duplicate entry: The book already exists."
        self.books.append(new_book)
        return "Book added successfully."

    def update_book(self, title, author, isbn, new_title=None, new_author=None, new_isbn=None):
        for book in self.books:
            if book.title == title and book.author == author and book.isbn == isbn:
                book.title = new_title if new_title else book.title
                book.author = new_author if new_author else book.author
                book.isbn = new_isbn if new_isbn else book.isbn
                return "Book updated successfully."
        return "Book not found."

    def delete_book(self, title, author, isbn):
        book_to_delete = next((b for b in self.books if b.title == title and b.author == author and b.isbn == isbn), None)
        if book_to_delete:
            self.books.remove(book_to_delete)
            return "Book deleted successfully."
        return "Book not found."

    def list_books(self):
        for book in self.books:
            print(book)

    def search_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def search_by_isbn(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)
