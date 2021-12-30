from validate_input import validate_input_number

# A function that let users to rate a book
def rating(books_list):
    """
    This function will make the customer to rate a book in the range of 1-5
    :param books_list: the list of books in our database (list)
    :return: None
    """
    # Ask the users the id of the book they want to rate
    rate_id = validate_input_number('Please enter the id of the book you want to rate: ', 0, len(books_list) - 1)
    
    # A loop to find the book users want to rate
    for book in books_list:
        # Found the book they want to rate
        if book["id"] == int(rate_id):
            print('You are rating the book ', book['name'])
            
            # Ask them to rate the book
            rating = validate_input_number('Please give us your rating for this book (0-5): ', 0, 5)

            # If there was no rates before, change it to rates of the users
            if book['average_rate'] == 'N/A':
                book['average_rate'] = rating

            # Else, update the the average rate of this book
            else:
                book['average_rate'] = (book['average_rate'] * book['num_of_rates'] + rating) / (
                        book['num_of_rates'] + 1)

            # Update the number of rates
            book['num_of_rates'] += 1
            
            print('Thank you for rating this book!')
            print('The current average rate for this book is', book['average_rate'])
            
            break
