# Feature 1: List all items:
def list_all_books(books_list):
    print("All books available:")
    for book in books_list:
        print(book["id"], "|", book["name"])