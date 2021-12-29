from utilities import validate_input_string


def sort_name(books_list):
    """
    This function will sort the book based on the book's name
    :param books_list: the list of books in our database
    :return: None
    """
    print('Please choose to sort books by name in descending or ascending order.')
    print("""
        asc - ascending
        des - descending
    """)
    # ask the user to choose a sorting order(ascending or descending)
    order = validate_input_string('Choose sorting order: ', "Please only choose between 'asc' or 'des'!",
                                  ['asc', 'des'])
    reversed = False if order == 'asc' else True
    sort_name_list = sorted(books_list, key=lambda x: x["name"], reverse=reversed)
    # printing the sorted book list by name
    for book in sort_name_list:
        print(f'Id: {book["id"]} | Name: {book["name"]}')


def sort_author(books_list):
    """
    This function will sort the book based on the author name
    :param book_list: the list of books in our database
    :return: None
    """
    print('Please choose to sort books by author in descending or ascending order.')
    print("""
        asc - ascending
        des - descending
    """)
    # ask the user to choose a sorting order(ascending or descending)
    order = validate_input_string('Choose sorting order: ', "Please only choose between 'asc' or 'des'!",
                                  ['asc', 'des'])
    reversed = False if order == 'asc' else True
    sort_author_list = sorted(books_list, key=lambda x: x["author"], reverse=reversed)
    # printing the sorted book list
    for book in sort_author_list:
        print(f'Id: {book["id"]} | Name: {book["name"]} | Author: {book["author"]}')


def sort_price(books_list):
    """
    This function will sort the book based on the price
    :param book_list: the list of books in our database
    :return: None
    """
    print('Please choose to sort books by price in descending or ascending order.')
    print("""
        asc - ascending
        des - descending
    """)
    # ask the user to choose a sorting order
    order = validate_input_string('Choose sorting order: ', "Please only choose between 'asc' or 'des'!",
                                  ['asc', 'des'])
    reversed = False if order == 'asc' else True
    sort_pricelist = sorted(books_list, key=lambda x: x["price"], reverse=reversed)
    # printing the sorted book list
    for book in sort_pricelist:
        print(f'Id: {book["id"]} | Name: {book["name"]} | Price: {book["price"]}')


def sort(books_list):
    """
    This function will make the customer to decide sorting the book list based on which category
    :param book_list: the list of books in our database
    :return: None
    """
    print('Please choose to sort books by name, author or prize.')
    # ask the user to choose a sorting method
    sort_type = validate_input_string('Choose sorting type: ',
                                      "Please only choose between 'name', 'author' or 'price'!",
                                      ['name', 'author', 'price'])
    if sort_type == 'name':
        sort_name(books_list)
    elif sort_type == 'author':
        sort_author(books_list)
    elif sort_type == 'price':
        sort_price(books_list)
