from utilities import *


def rating(books_list):
    id = validate_input_number('Please enter the id of the book you want to rate: ', 'Please enter a correct book ID',
                               len(books_list) - 1)
    for book in books_list:
        if book["id"] == int(id):
            print('You are rating the book ', book['name'])
            rating = validate_input_number('Please give us your rating for this book (0-5): ',
                                           'Please only enter a number from 0-5', 5)
            if book['average_rate'] == 'N/A':
                book['average_rate'] = rating
            else:
                book['average_rate'] = (book['average_rate'] * book['num_of_rates'] + rating) / (
                            book['num_of_rates'] + 1)
            book['num_of_rates'] += 1
            print('Thank you for rating this book!')
            print('The current average rate for this book is', book['average_rate'])
            break
