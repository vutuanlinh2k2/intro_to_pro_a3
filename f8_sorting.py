from validate_input import validate_input_string
from get_data import get_books_data

# Function 8: Sorting


def sort_name(books_list):
    """
    This function will sort the book based on the book's name
    :param books_list: the list of books in our database (list)
    :return: None
    """

    print('Please choose to sort books by name in descending or ascending order.')
    print("""
        asc - ascending
        des - descending
    """)

    # Ask the user to choose a sorting order (ascending or descending)
    order = validate_input_string('Choose sorting order: ', "Please only choose between 'asc' or 'des'!",
                                  ['asc', 'des'])
    reversed = False if order == 'asc' else True
    # sort books by name in either ascending or descending order
    sort_name_list = sorted(books_list, key=lambda x: x["name"], reverse=reversed)

    # Printing the sorted book list by name
    for book in sort_name_list:
        print('Id: {0:>2} | Name: {1}'.format(book["id"], book["name"]))


def sort_author(books_list):
    """
    This function will sort the book based on the author name
    :param books_list: the list of books in our database (list)
    :return: None
    """

    print('Please choose to sort books by author in descending or ascending order.')
    print("""
        asc - ascending
        des - descending
    """)

    # Ask the user to choose a sorting order(ascending or descending)
    order = validate_input_string('Choose sorting order: ', "Please only choose between 'asc' or 'des'!",
                                  ['asc', 'des'])
    reversed = False if order == 'asc' else True
    # sort books by author name in either ascending or descending order
    sort_author_list = sorted(books_list, key=lambda x: x["author"], reverse=reversed)

    # Printing the sorted book list
    for book in sort_author_list:
        print('Id: {0:>2} | Name: {1} | Author: {2}'.format(
            book["id"], book["name"], book["author"]))


def sort_price(books_list):
    """
    This function will sort the book based on the price
    :param books_list: the list of books in our database (list)
    :return: None
    """
    print('Please choose to sort books by price in descending or ascending order.')
    print("""
        asc - ascending
        des - descending
    """)

    # Ask the user to choose a sorting order
    order = validate_input_string('Choose sorting order: ', "Please only choose between 'asc' or 'des'!",
                                  ['asc', 'des'])
    reversed = False if order == 'asc' else True
    # sort books by price in either ascending or descending order
    sort_pricelist = sorted(books_list, key=lambda x: x["price"], reverse=reversed)

    # Printing the sorted book list
    for book in sort_pricelist:
        print('Id: {0:>2} | Name: {1} | Price: {2}'.format(
            book["id"], book["name"], book["price"]))


def sort():
    """
    This function will make the customer to decide sorting the book list based on which category
    :param: None
    :return: None
    """
    # Get the book list from other file
    books_list = get_books_data()

    # Ask the user to choose a sorting method
    print('Please choose to sort books by name, author or price.')
    sort_type = validate_input_string('Choose sorting type: ',
                                      "Please only choose between 'name', 'author' or 'price'!",
                                      ['name', 'author', 'price'])
    if sort_type == 'name':
        sort_name(books_list)
    elif sort_type == 'author':
        sort_author(books_list)
    elif sort_type == 'price':
        sort_price(books_list)
