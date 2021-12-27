from books import *
from utilities import *

# basic features
from f1_list_all_items import *
from f2_item_info import *
from f3_search_name import *
from f4_search_id import *
from f5_customer_info import *
from f6_place_order import *

# advanced features
from f7_filtering import *
from f8_sorting import *
from f9_rates import *
# the feature vouchers goes with place_order feature

customers = []

print('Welcome to our book store. Please enter a number correspond to any action as shown below!')
while True:
    print("""
        0 - List all books
        1 - List all info of a specific book
        2 - Search item by name
        3 - Search item by id
        4 - List all info of a specific customer
        5 - Place order
        6 - Filtering
        7 - Sorting
        8 - Rates
        9 - Quit
    """)
    n = validate_input_number("Which action do you want to perform?: ", 'Your input is not valid. Please only enter a number between 0 and 9!', 9)
    if n == 0:
        list_all_books(books_list)
    elif n == 1:
        book_info(books_list)
    elif n == 2:
        name_search(books_list)
    elif n == 3:
        id_search(books_list)
    elif n == 4:
        customer_info(customers)
    # elif n == 5:
    elif n == 6:
        filter(books_list)
    elif n == 7:
        sort(books_list)
    elif n == 8:
        rating(books_list)
    else:
        print("Thank you for visiting our store. We hope to see you back soon!")
        break
    
