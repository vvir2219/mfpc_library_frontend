from api import API, api_members, base_url, api_books
from menu import menu, menu_item, api_menu
from books import book_repr, borrow_book
from borrows import borrow_repr, return_borrow

def member_repr(member):
    return f"\nId: {member['id']}\nName: {member['name']}"

def member_borrow_book(member):
    def borrow(book):
        response = borrow_book(book['id'], member['id']).json()
        if response['success']:
            print("You have borrowed the book!")
        else:
            print(response['message'])
    return borrow

def member_return_book(member):
    def do_return(borrow):
        response = return_borrow(borrow['id']).json()
        if response['success']:
            print("You have returned the book!")
        else:
            print(response['message'])
    return do_return

def member_books_menu(member):
    return api_menu(
        get_items=lambda: api_books.get('available').json(),
        no_items_message="There are no available books to borrow!",
        item_command=lambda book: f"borrow {book['id']}",
        item_repr=book_repr,
        item_func=member_borrow_book(member)
    )

def member_search_books_menu(member):
    search_term = input("Search term: ")

    return api_menu(
        get_items=lambda: api_books.get(f"search?query={search_term}&available=1").json(),
        no_items_message="No suitable books found available to borrow!",
        item_command=lambda book: f"borrow {book['id']}",
        item_repr=book_repr,
        item_func=member_borrow_book(member)
    )

def member_borrows_menu(member):
    return api_menu(
        get_items=lambda: api_members.get(f"{member['id']}/borrows?returned=0").json(),
        no_items_message="No books borrowed!",
        item_command=lambda borrow: f"return {borrow['id']}",
        item_repr=borrow_repr,
        item_func=member_return_book(member)
    )

def member_menu(member_id):
    member = api_members.get(member_id).json()
    if member is None:
        print('Invalid member card id')
        exit(1)

    api_member = API(base_url + 'members' + '/' + member_id)

    return menu(
        top_message=f"[ MAIN MENU ]\n\nHello {member['name']}. What can I help you with today?\n",
        prompt='\nInput command: ',
        menu_items={
            'books': menu_item("Check out books", lambda: member_books_menu(member)),
            'search': menu_item("Search books to borrow", lambda: member_search_books_menu(member)),
            'borrows': menu_item("Check out my borrows", lambda: member_borrows_menu(member))
        }
    )

