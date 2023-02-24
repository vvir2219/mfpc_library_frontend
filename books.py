from datetime import datetime, timedelta
from api import api_borrows, api_books

def book_repr(book):
    return f"\nTitle: {book['title']}\nAuthor: {book['author']}\n"

def borrow_book(book_id, member_id):
    return api_borrows.post(
        body={
            'book_id': book_id,
            'member_id': member_id,
            'expiration_date': datetime.now() + timedelta(days=21)
        })

def create_book(title, author):
    return api_books.post(
        body={
            'title': title,
            'author': author,
        })

def destroy_book(book_id):
    return api_books.delete(str(book_id))
