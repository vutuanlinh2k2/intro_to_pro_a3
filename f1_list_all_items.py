# Feature 1: List all items:

def list_all_books(books_list):
    """
    This function will list all the books of our store (including their name and ID)
    :param books_list: the list of book in our database
    :return: None
    """
    print("All books available:")
    for book in books_list:
        print("{0:>2} {1} {2}".format(book["id"], "|", book["name"]))   # Format string to align the book list perfectly
