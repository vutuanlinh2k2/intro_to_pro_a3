# Feature 1: List all items:
"""
This function will
: param
: return
"""
def list_all_books(books_list):
    print("All books available:")
    for book in books_list:
        print("{0:>2} {1} {2}".format(book["id"], "|", book["name"]))   # Format string to align the book list perfectly
