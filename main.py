#Main.py calls all the classes and functions and performs all the actions accordingly.

from book import Books
from user import Users
from check import Record
from storage import Storage
import datetime

# Initialize the management systems
book_management = Books()
user_management = Users()
#record_management = Record(book_management)
record_management = Record(book_management, user_management)

# Initialize the storage system
storage_management = Storage('storage/books.csv', 'storage/users.csv', 'storage/records.csv', book_management, user_management, record_management)
storage_management.load()

class Logger:
    """
    Simple Logger for logging events and actions within the system.
    """
    def __init__(self, log_file='storage/library_app.log'):
        self.log_file = log_file

    def log(self, msg):
        """
        Logs a message with a timestamp to the log file.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a+') as file:
            file.write(f"[{timestamp}] {msg}\n")

logger = Logger()


#Add teh books and details
def add_book():
    print("Please provide the details of the book to add:")
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    qty = int(input("Enter quantity: "))
    message = book_management.add_book(title, author, isbn, qty)
    if message == "Book added successfully.":
        storage_management.save()
    print(message)
    logger.log(f"{message}: {title} by {author}, ISBN: {isbn}, Quantity: {qty}")


#Lists out all the books stored in our database
def list_books():
    print("\nListing all books:")
    if not book_management.books:
        print("No books available.")
    else:
        for book in book_management.books:
            print(book)


#Searches for the books (Based on title or ISBN)
def search_book():
    print("1. Search by title\n2. Search by ISBN")
    choice = input("Select an option: ")
    if choice == "1":
        title = input("Enter book title: ")
        books = book_management.search_by_title(title)
        if books:
            for book in books:
                print(book)
        else:
            print("No books found with that title.")
        logger.log(f"Searched for book by title: {title}")
    elif choice == "2":
        isbn = input("Enter ISBN: ")
        book = book_management.search_by_isbn(isbn)
        if book:
            print(book)
        else:
            print("No books found with that ISBN.")
        logger.log(f"Searched for book by ISBN: {isbn}")


#Updates the book details 
def update_book():
    print("Please provide the current details of the book:")
    title = input("Enter current title: ")
    author = input("Enter current author: ")
    isbn = input("Enter current ISBN: ")
    new_title = input("Enter new title (leave blank to keep current): ")
    new_author = input("Enter new author (leave blank to keep current): ")
    new_isbn = input("Enter new ISBN (leave blank to keep current): ")
    message = book_management.update_book(title, author, isbn, new_title or None, new_author or None, new_isbn or None)
    if message == "Book updated successfully.":
        storage_management.save()
    print(message)
    logger.log(message)


#Deletes the required book
def delete_book():
    print("Please provide the details of the book to delete:")
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    message = book_management.delete_book(title, author, isbn)
    if message == "Book deleted successfully.":
        storage_management.save()
    print(message)
    logger.log(message)

#Add the users
def add_user():
    name = input("Enter user name: ")
    user_id = input("Enter user ID: ")
    message = user_management.add_user(name, user_id)
    storage_management.save()
    print(message)
    logger.log(f"Added user: Name: {name}, ID: {user_id}")

#Lists the users
def list_users():
    print("\nListing all users:")
    if not user_management.users:
        print("No users available.")
    else:
        for user in user_management.users:
            print(user)

#Searches for the users by username or userID (Ones own choice)
def search_user():
    print("1. Search by name\n2. Search by user ID")
    choice = input("Select an option: ")
    if choice == "1":
        name = input("Enter user name: ")
        users = user_management.search_by_name(name)
        if users:
            for user in users:
                print(user)
        else:
            print("No users found with that name.")
        logger.log(f"Searched for user by name: {name}")
    elif choice == "2":
        user_id = input("Enter user ID: ")
        user = user_management.search_by_id(user_id)
        if user:
            print(user)
        else:
            print("No users found with that ID.")
        logger.log(f"Searched for user by ID: {user_id}")

#Deletes the user
def delete_user():
    user_id = input("Enter user ID to delete: ")
    message = user_management.delete_user(user_id)
    if message:
        storage_management.save()
        print("User deleted successfully.")
    else:
        print("User not found.")
    logger.log(f"Deleted user: ID: {user_id}")


#Checks for the checkout details if the user is registered 
def checkout_book():
    user_id = input("Enter user ID: ")
    isbn = input("Enter ISBN of the book to checkout: ")
    message = record_management.checkout_book(user_id, isbn)
    print(message)
    if "successfully" in message:
        storage_management.save()
    logger.log(f"Checkout: {message}")

#Checks for the Checkin details of the book details based on its checkout details and calculates the renewal date and late fee
    user_id = input("Enter user ID: ")
    isbn = input("Enter ISBN of the book to check in: ")
    message = record_management.checkin_book(user_id, isbn)
    print(message)
    if "successfully" in message:
        storage_management.save()
    logger.log(f"Checkin: {message}")

def checkin_book():
    user_id = input("Enter user ID: ")
    isbn = input("Enter ISBN of the book to check in: ")
    message = record_management.checkin_book(user_id, isbn)
    print(message)
    if "successfully" in message:
        storage_management.save()
    logger.log(f"Checkin: {message}")

#Lists all the checkins and checkouts
def list_records():
    print("\nListing all records:")
    if not record_management.records:
        print("No records available.")
    else:
        for record in record_management.records:
            print(record)

#Selectable menu options for the users
def main_menu():
    options = {
        "1": add_book,
        "2": search_book,
        "3": update_book,
        "4": delete_book,
        "5": add_user,
        "6": search_user,
        "7": delete_user,
        "8": checkout_book,
        "9": checkin_book,
        "10": list_books,
        "11": list_users,
        "12": list_records,
        "13": exit
    }
    while True:
        print("\nLibrary Management System")
        print("1: Add Book\n2: Search Book\n3: Update Book\n4: Delete Book")
        print("5: Add User\n6: Search User\n7: Delete User")
        print("8: Checkout Book\n9: Checkin Book")
        print("10: List Books\n11: List Users\n12: List Records")
        print("13: Exit")
        choice = input("Enter your choice: ")
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
