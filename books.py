from datetime import datetime, timedelta
from api import api_borrows

def book_repr(book):
    return f"\nTitle: {book['title']}\nAuthor: {book['author']}\n"

def borrow_book(book_id, member_id):
    return api_borrows.post(
        body={
            'book_id': book_id,
            'member_id': member_id,
            'expiration_date': datetime.now() + timedelta(days=21)
        })
