from get_data import get_books_data

# Feature 1: List all items:


def list_all_books():
    """
    This function will list all the books of our store (including their name and ID)
    :param: None
    :return: None
    """
    # Get the book data from other file
    books_list = get_books_data()
    print("All books available:")

    # Loop through each book in the book list
    for book in books_list:
        # Format string to align the book list perfectly
        print("{0:>2} {1} {2}".format(book["id"], "|", book["name"]))
