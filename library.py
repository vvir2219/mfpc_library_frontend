#!/usr/local/bin/python3

import sys
from member import member_menu
from members import member_repr
from librarian import librarian_menu
from api import api_members


# MAIN

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ./library.py [ librarian | members | member <member-id> ]')
        exit(1)

    if sys.argv[1] == 'librarian':
        librarian_menu()
    elif sys.argv[1] == 'member':
        if len(sys.argv) < 3:
            print('Usage: ./library.py [ librarian | member <member-id> ]')
        else:
            member_menu(sys.argv[2])
    elif sys.argv[1] == 'members':
        members = api_members.get().json()
        for member in members:
            print(member_repr(member))
    else:
        print('Usage: ./library.py [ librarian | members | member <member-id> ]')
