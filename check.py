#In the below class and functions, we mentioned a clause where the checkout happens only if the user/ISBN is present and also if the user's checkout date crosses more than 30 days then 1 rupee per each day is costed as a late fee

from datetime import datetime, timedelta

class Record:
    def __init__(self, book_management, user_management):
        self.book_management = book_management
        self.user_management = user_management
        self.records = []

    def checkout_book(self, user_id, isbn):
        # Check if the user exists and is currently registered
        user = self.user_management.search_by_id(user_id)
        if not user:
            return "User not found or is not active."

        book = self.book_management.search_by_isbn(isbn)
        if book and book.qty > 0:
            book.qty -= 1
            due_date = datetime.now() + timedelta(days=30) #calculates the renewal/due date
            self.records.append({'user_id': user_id, 'isbn': isbn, 'action': 'checkout', 'due_date': due_date})
            return "Book checked out successfully. Due date: " + due_date.strftime('%Y-%m-%d')
        return "Book not found or unavailable."

    def checkin_book(self, user_id, isbn):
        #Check if the checkin done before due date or else the user will be fined
        record = next((r for r in self.records if r['user_id'] == user_id and r['isbn'] == isbn and r['action'] == 'checkout'), None)
        if record:
            book = self.book_management.search_by_isbn(isbn)
            if book:
                book.qty += 1
                overdue_days = max(0, (datetime.now() - record['due_date']).days - 30)
                overdue_fee = overdue_days * 1
                self.records.append({'user_id': user_id, 'isbn': isbn, 'action': 'checkin'})
                return "Book checked in. Overdue fee: Rs." + str(overdue_fee)
            return "Book not found."
        return "No checkout record found."
