from get_data import get_books_data

# Feature 4: Search book by Id


def id_search():
    """
    This function will help the customer to search a book by typing its ID
    :param: None
    :return: None
    """
    # Get the book data from other file
    books_list = get_books_data()

    # Ask customers the id of the book they want to search
    search_id = input("Enter the id of the book you want to search: ")
    num = 0

    # Loop through each book in the book list
    for book in books_list:      
        if book["id"] == int(search_id):

            # Print the information of the chosen book
            print('\n')
            print("Id:", book["id"], "| Name:", book["name"], "| Author:",
                  book["author"], "| Quantity:", book["quantity"])
            num += 1

    # In case the chosen book's id is not in our store's database
    if num == 0:
        print("We can't find any book with that id")
