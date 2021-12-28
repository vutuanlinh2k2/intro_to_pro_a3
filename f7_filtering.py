from utilities import *


def filter_genre(books_list):
    """
    This function will filter the book list by genre
    :param books_list: the list of book in our database
    :return: None
    """
    genre_list = []
    for book in books_list:
        for genre in book["genre"]:
            if genre not in genre_list:
                genre_list.append(genre)

    print('All the genres available include:')
    for genre in genre_list:
        print(genre)
    chosen_genre = validate_input_string(
        "Please choose a genre: ", 'Please choose a correct genre', genre_list)
    for book in books_list:
        if chosen_genre.lower() in book["genre"]:
            print("Id:", book["id"], "| Name:",
                  book["name"], "| Author:", book["author"])


def filter_pages(books_list):
    """
    This function will filter the book list by the number of pages
    :param books_list: the list of book in our database
    :return: None
    """
    num = 0
    minimum_page_numbers = validate_input_number('Enter the minimum pages: ', 0, 100000)
    maximum_page_numbers = validate_input_number('Enter the maximum pages: ', 0, 10000)
    while maximum_page_numbers < minimum_page_numbers:
        print('The maximum pages should be bigger than the minimum!')
        maximum_page_numbers = validate_input_number('Enter the maximum pages: ', 0, 10000)
    for book in books_list:
        if minimum_page_numbers <= book["pages"] <= maximum_page_numbers:
            print("Id:", book["id"], "| Name:", book["name"],
                  "| Author:", book["author"], "| Pages:", book["pages"])
            num += 1
    if num == 0:
        print("We can't find any book satisfying the chosen criteria")


def filter_price(books_list):
    """
    This function will filter the book list by price
    :param books_list: the list of book in our database
    :return: None
    """
    num = 0
    minimum_price = validate_input_number('Enter the minimum price: ', 0, 100)
    maximum_price = validate_input_number('Enter the maximum price: ', 0, 100)
    while maximum_price < minimum_price:
        print('The maximum price should be bigger than the minimum')
        maximum_price = validate_input_number('Enter the maximum pages: ', 0, 100)
    for book in books_list:
        if minimum_price <= book["price"] < maximum_price:
            print("Id:", book["id"], "| Name:", book["name"],
                  "| Author:", book["author"], "| Price: $", book["price"])
            num += 1
    if num == 0:
        print("We can't find any book satisfying the chosen criteria")


def filter(books_list):
    """
    This function will make the customer to decide filter by which category
    :param books_list: the list of book in our database
    :return: None
    """
    print('Please choose to filter books by genre, pages or price.')
    sort_type = validate_input_string('Choose filter type: ', "Please only choose between 'genre', 'pages' or 'price'!",
                                      ['genre', 'pages', 'price'])
    if sort_type == 'genre':
        filter_genre(books_list)
    elif sort_type == 'pages':
        filter_pages(books_list)
    elif sort_type == 'price':
        filter_price(books_list)
