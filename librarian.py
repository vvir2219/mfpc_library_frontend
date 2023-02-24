from books import create_book,destroy_book,book_repr
from menu import menu,menu_item,api_menu
from api import api_books,api_borrows,api_members
from members import create_member,member_repr
from borrows import borrow_repr

def librarian_remove_book(book):
    response = destroy_book(book['id']).json()
    if response['success']:
        print("You have removed the the book!")
    else:
        print(response['message'])

def librarian_new_book():
    title = input("Title: ")
    author = input("Author: ")
    response = create_book(title, author).json()
    if response['success']:
        print("A new book has been added to the library!")
    else:
        print(response["message"])

def librarian_books_menu():
    return api_menu(
        get_items=lambda: api_books.get().json(),
        no_items_message="There are no books. What a sad library.",
        item_command=lambda book: f"remove {book['id']}",
        item_repr=book_repr,
        item_func=librarian_remove_book
    )

def librarian_search_books_menu():
    search_term = input("Search term: ")
    return api_menu(
        get_items=lambda: api_books.get(f"search?query={search_term}&available=1").json(),
        no_items_message="No book found by search term",
        item_command=lambda book: f"remove {book['id']}",
        item_repr=book_repr,
        item_func=librarian_remove_book
    )

def librarian_new_member():
    name = input("Name: ")
    response = create_member(name).json()
    if response['success']:
        print("A new member has been added to the library")
        print(member_repr(response['member']))
    else:
        print(response["message"])

def librarian_borrows():
    borrows = api_borrows.get('?returned=0').json()
    if len(borrows) == 0:
        print("No books to be returned!")
    else:
        for borrow in borrows:
            print(borrow_repr(borrow))


def librarian_borrows_by_member():
    member_id = input("Member id: ")
    borrows = api_members.get(f"{member_id}/borrows?returned=0").json()
    if len(borrows) == 0:
        print("No books to be returned!")
    else:
        for borrow in borrows:
            print(borrow_repr(borrow))


def librarian_menu():
    return menu(
        top_message=f"[ MAIN MENU ]\n",
        prompt='\nInput command: ',
        menu_items={
            'new book': menu_item("Add a new book to the library", librarian_new_book),
            'books': menu_item("View all books", librarian_books_menu),
            'search': menu_item("Search book by title/author", librarian_search_books_menu),

            'new member': menu_item("Create new membership card", librarian_new_member),
            'borrows': menu_item("See all borrowed books", librarian_borrows),
            'member borrows': menu_item("Check borrowed books of a certain member", librarian_borrows_by_member)
        }
    )

