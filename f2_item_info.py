from validate_input import validate_input_number
from get_data import get_books_data

# Feature 2: List all items' information:


def book_info():
    """
    This function will provide all the information of a specific book (including name, author, genre, description, price and rating)
    :param books_list: the list of books in our database (list)
    :return: None
    """
    books_list = get_books_data()
    # Ask the user for the id of the book that they want to see
    book_id = validate_input_number(
        "Enter the ID of the book that you want to see: ", 1, len(books_list))
    selected_book = books_list[int(book_id)]
    print(selected_book['name'], 'written by', selected_book['author'])
    print('Genre:', selected_book['genre'],
          '| Number of pages:', selected_book['pages'])
    print(selected_book['description'])
    print('Price: $', selected_book['price'],
          '| Quantity:', selected_book['quantity'])
    print('Avarage ratings:', selected_book['average_rate'],
          '| Number of rates: ', selected_book['num_of_rates'])
