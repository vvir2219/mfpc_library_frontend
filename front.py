#Carti:
#- id
#- titlu
#- autor
#- available
#
#Abonament:
#- id
#- nume
#
#Imprumuturi:
#- id
#- id carte
#- id abonament
#- data incepere
#- data expirare
#
#Functionalitati:
#1. Adaugare carte
#2. Eliminare carte
#3. Cauta dupa titlu si/sau autor
#4. Creaza abonament
#5. Imprumuta carte
#6. Returneaza carte
#7. Vezi carti imprumutate de abonat cu data de expirare

import requests
import json

api_url = "http://192.168.0.171:3000/"
api_url = "http://localhost:3000/"

def api_add_book(title, author):
    j = {'title': title, 'author': author}
    requests.post(api_url + 'books', j)

def api_delete_book(index):
    requests.delete(api_url + f'books/{index}')

def api_get_books(query):
    response = requests.get(api_url + f'books/search?query={query}&available=1')
    return response.json()

def api_get_available_books():
    response = requests.get(api_url + 'books/available')
    return response.json()

def api_create_membership(owner):
    j = {'owner': owner}
    requests.post(api_url + 'members', j)

def api_get_memberships():
    response = requests.get(api_url + 'members')
    return response.json()

def api_add_borrow_book(book, member, expiration_date):
    j = {'book_id': book, 'member_id': member, 'expiration_date': expiration_date}
    requests.post(api_url + 'borrows', j)

def api_delete_borrowed_book(index):
    response = requests.post(api_url + f'borrows/{index}/return')

def api_get_borrowed_by_member(member):
    response = requests.get(api_url + f'members/{member}/borrows')
    return response.json()

def add_book():
    title = input("Insert Book title:")
    author = input("Insert Book author:")
    api_add_book(title, author)

def remove_book():
    index = int(input("Insert Book index:"))
    api_delete_book(index)

def see_available_books():
    books = api_get_available_books()
    print(*books, sep = "\n")

def see_books():
    query = input("Query :")
    books = api_get_books(query)
    print(*books, sep = "\n")

def create_membership():
    name = input("Insert Member name :")
    api_create_membership(name)

def see_memberships():
    memberships = api_get_memberships();
    print(*memberships, sep = "\n")

def borrow_book():
    book = input("Insert Book index:")
    member = input("Insert Member index:")
    expiration_date= input("Insert expiration date:")
    api_add_borrow_book(book, member, expiration_date)

def return_Book():
    index = input("Insert Borrow index: ")
    api_delete_borrowed_book(index)

def see_borrowed_by_member():
    member = input("Insert Member index:")
    borrows = api_get_borrowed_by_member(member)
    print(*borrows, sep = "\n")

def main():
    menu = {}
    menu['1'] = add_book
    menu['2'] = remove_book
    menu['3'] = see_books
    menu['4'] = see_available_books
    menu['5'] = create_membership
    menu['6'] = see_memberships
    menu['7'] = borrow_book
    menu['8'] = return_Book
    menu['9'] = see_borrowed_by_member
    menu['0'] = exit

    while True:
        print("Book library:")
        print("1. Add book")
        print("2. Remove book")
        print("3. See books by query")
        print("4. See all available books")
        print("5. Create membership")
        print("6. See memberships")
        print("7. Borrow book")
        print("8. Return book")
        print("9. See borrowed books by member")
        print("0. Exit")

        option = input("- ")
        if option in menu:
            menu[option]()
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
