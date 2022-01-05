from validate_input import validate_input_number
from get_data import get_books_data

# Feature 2: List all items' information:


def book_info():
    """
    This function will provide all the information of a specific book (including name, author, genre, number of pages, description, price and rating)
    :param: None
    :return: None
    """
    # Get the book data from other file
    books_list = get_books_data()

    # Ask the user for the id of the book that they want to see
    book_id = validate_input_number(
        "Enter the ID of the book that you want to see: ", 1, len(books_list))

    # Idenfiy the chosen book in the book list    
    selected_book = books_list[int(book_id)]

    # Print all the information of the chosen book
    print("\nHere is the detailed information of the book you require: \n")
    print("Name:" ,selected_book['name'], '| Author:', selected_book['author'])
    print('Genre:', selected_book['genre'],
          '| Number of pages:', selected_book['pages'])
    print("\nDescription:", selected_book['description'])
    print('Price: $', selected_book['price'],
          '| Quantity:', selected_book['quantity'])
    print('Avarage ratings:', selected_book['average_rate'],
          '| Number of rates: ', selected_book['num_of_rates'])
