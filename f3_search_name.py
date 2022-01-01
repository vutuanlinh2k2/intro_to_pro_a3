from get_data import get_books_data
# Feature 3: Search book by name


def name_search():
    """
    This function will help the customer to search a book by typing the book's name or words in the name
    :param: None
    :return: None
    """

    # Get the book data from other file
    books_list = get_books_data()

    # Ask customers the name of the book they want to search
    search_name = input("Enter the name of the book you want to search: ")
    num = 0

    # Loop through each book in the book list
    for book in books_list:
        if search_name.lower() in book["name"].lower():

            # Print the information of the chosen book
            print("Id:", book["id"], "| Name:", book["name"], "| Author:",
                  book["author"], "| Quantity:", book["quantity"])

            num += 1    

    # In case the chosen book's name is not in our store's database
    if num == 0:
        print("We can't find any book with that name!")
