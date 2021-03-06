from validate_input import *
from get_data import get_books_data

# Function 7: Filtering


def filter_genre(books_list):
    """
    This function will filter the book list by genre
    :param books_list: the list of books in our database (list)
    :return: None
    """
    # Create the genre list
    genre_list = []
    # Add all genres of books in our database to the genre list
    for book in books_list:
        for genre in book["genre"]:
            if genre not in genre_list:
                genre_list.append(genre)

    # Showcase all the genres for the users to choose from
    print('\nAll the genres available include:')
    for genre in genre_list:
        print(genre)

    # Get the user's option
    chosen_genre = validate_input_string(
        "\nPlease choose a genre: ", 'Please choose a correct genre', genre_list)

    # Print the books that match that genre
    print('\n')
    for book in books_list:
        if chosen_genre.lower() in book["genre"]:
            print("Id: {0:>2}".format(book["id"]), "| Name:",
                  book["name"], "| Author:", book["author"])


def filter_pages(books_list):
    """
    This function will filter the book list by the number of pages
    :param books_list: the list of books in our database (list)
    :return: None
    """
    num = 0
    # Get the user's data
    minimum_page_numbers = validate_input_number(
        '\nEnter the minimum pages: ', 0, 10000)
    maximum_page_numbers = validate_input_number(
        'Enter the maximum pages: ', 0, 10000)

    # Get the user's data again if the minimum pages number is larger than the maximum one
    while maximum_page_numbers < minimum_page_numbers:
        print('The maximum pages should be bigger than the minimum!')
        maximum_page_numbers = validate_input_number(
            'Enter the maximum pages: ', 0, 10000)

    # Sorting the books given the minimum and maximum pages number
    print('\n')
    for book in books_list:
        if minimum_page_numbers <= book["pages"] <= maximum_page_numbers:
            print("Id: {0:>2}".format(book["id"]), "| Name:", book["name"],
                  "| Author:", book["author"], "| Pages:", book["pages"])
            num += 1

    # If there are no books that satisfy the input number
    if num == 0:
        print("We can't find any book satisfying the chosen criteria")


def filter_price(books_list):
    """
    This function will filter the book list by price
    :param books_list: the list of books in our database (list)
    :return: None
    """
    num = 0
    # Get the user's data
    minimum_price = validate_input_number('\nEnter the minimum price: ', 0, 100)
    maximum_price = validate_input_number('Enter the maximum price: ', 0, 100)

    # Get the user's data again if the minimum price is larger than the maximum one
    while maximum_price < minimum_price:
        print('The maximum price should be bigger than the minimum')
        maximum_price = validate_input_number(
            'Enter the maximum pages: ', 0, 100)

    # Sorting the books given the minimum and maximum price
    print('\n')
    for book in books_list:
        if minimum_price <= book["price"] < maximum_price:
            print("Id: {0:>2}".format(book["id"]), "| Name:", book["name"],
                  "| Author:", book["author"], "| Price: $", book["price"])
            num += 1

    # If there are no books that satisfy the input number
    if num == 0:
        print("We can't find any book satisfying the chosen criteria")


def filter():
    """
    This function will make the customer to decide filter by which category
    :param: None
    :return: None
    """
    # Get the book l??st from other file
    books_list = get_books_data()

    # Ask the user to choose a filter method
    print('\nPlease choose to filter books by genre, pages or price.')
    sort_type = validate_input_string('Choose filter type: ', "\nPlease only choose between 'genre', 'pages' or 'price'!",
                                      ['genre', 'pages', 'price'])
    if sort_type == 'genre':
        filter_genre(books_list)
    elif sort_type == 'pages':
        filter_pages(books_list)
    elif sort_type == 'price':
        filter_price(books_list)
