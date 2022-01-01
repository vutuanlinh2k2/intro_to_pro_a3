from validate_input import validate_input_number
from get_data import get_books_data
from update_data import update_book_rate

# A function that let users to rate a book
def rating():
    """
    This function will make the customer to rate a book in the range of 1-5
    :param: None
    :return: None
    """
    # Ask the users the id of the book they want to rate
    books_list = get_books_data()
    rate_id = validate_input_number('Please enter the id of the book you want to rate: ', 1, len(books_list))
    
    # A loop to find the book users want to rate
    for book in books_list:
        # Found the book they want to rate
        if book["id"] == int(rate_id):
            print('You are rating the book ', book['name'])
            
            # Ask them to rate the book
            rating = validate_input_number('Please give us your rating for this book (1-5): ', 1, 5)

            update_book_rate(rate_id, rating)
            
            break
        


