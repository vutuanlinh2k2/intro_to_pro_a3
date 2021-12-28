# Feature 1: List all items:
def list_all_books(books_list):
    print("All books available:")
    for book in books_list:
        print("{0:>2} {1} {2}".format(book["id"], "|", book["name"]))