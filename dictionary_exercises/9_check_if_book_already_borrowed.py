#9- A library has a list of borrowed books. If someone tries to borrow a book that has already been borrowed, it should not be allowed.

def find_borrowed_book(book_availability, book_to_find):
    for book, availability in book_availability.items():
        if book == book_to_find:
            return availability

def test():
    is_available = None
    book_to_find = input("enter book to find: ")
    book_availability = {
        "harry potter": True,
        "peter pan": True,
        "mathematics 2": True,
        "physics 4": False,
        "physics 6": False,
    }

    availability = find_borrowed_book(book_availability, book_to_find)
    if availability == True:
        print(f"the book is available")
    else:
        print(f"the book is not available")

test()