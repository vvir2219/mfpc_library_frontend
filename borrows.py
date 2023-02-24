from api import api_borrows

def borrow_repr(borrow):
    repr = f"\nId: {borrow['id']}\nBook: {borrow['book_title']}\nBorrower: {borrow['member_name']}\nBorrowed at: {borrow['created_at']}\nBest returned before: {borrow['expiration_date']}\n"
    if 'returned_at' in borrow:
        repr += f"Returned at: {borrow['returned_at']}\n"
    return repr

def return_borrow(borrow_id):
    return api_borrows.post(f"{borrow_id}/return")
