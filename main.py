from books import *
from utilities import *

# basic features
from f1_list_all_items import *
from f2_item_info import *
from f3_search_name import *
from f4_search_id import *
from f5_customer_info import *
from f6_place_order import place_order

# advanced features
from f7_filtering import filter
from f8_sorting import sort
from f9_rates import *
# the feature vouchers goes with place_order feature

# a variable storing all customers' information
customers_list = []

print('Welcome to our book store!')

# a loop that let users do multiple actions before they quit
while True:
    
    # guiding users
    print('Please enter a number correspond to any action as shown below!')
    print("""
        1 - List all books
        2 - List all info of a specific book
        3 - Search item by name
        4 - Search item by id
        5 - List all info of a specific customer
        6 - Place order
        7 - Filtering
        8 - Sorting
        9 - Rates
        10 - Quit
    """)
    
    # let users choose their actions
    n = validate_input_number("Which action do you want to perform?: ", 1, 10)
    
    if n == 1:
        list_all_books(books_list)
    elif n == 2:
        book_info(books_list)
    elif n == 3:
        name_search(books_list)
    elif n == 4:
        id_search(books_list)
    elif n == 5:
        customer_info(customers_list)
    elif n == 6:
        place_order(books_list, customers_list)
    elif n == 7:
        filter(books_list)
    elif n == 8:
        sort(books_list)
    elif n == 9:
        rating(books_list)
    else:
        print("Thank you for visiting our store. We hope to see you back soon!")
        break
    
    # ask if user want to go back and perform other actions
    input('\nReady to change to other actions. Just click enter. ')
    
    # clear the screen
    for i in range(100):
        print('\n')
    
