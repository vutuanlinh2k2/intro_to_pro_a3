from validate_input import validate_input_number

# Basic features
from f1_list_all_items import list_all_books
from f2_item_info import book_info
from f3_search_name import name_search
from f4_search_id import id_search
from f5_customer_info import customer_info
from f6_place_order import place_order

# Advanced features
from f7_filtering import filter
from f8_sorting import sort
from f9_rating import rating
# The feature vouchers goes with place_order feature.

print('Welcome to our book store!')

# A loop that let users do multiple actions before they quit.
while True:
    
    # Guiding users
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
        9 - Rating
        10 - Quit
    """)
    
    # Let users choose their actions.
    n = validate_input_number("Which action do you want to perform?: ", 1, 10)
    
    if n == 1:
        list_all_books()
    elif n == 2:
        book_info()
    elif n == 3:
        name_search()
    elif n == 4:
        id_search()
    elif n == 5:
        customer_info()
    elif n == 6:
        place_order()
    elif n == 7:
        filter()
    elif n == 8:
        sort()
    elif n == 9:
        rating()
    else:
        print("Thank you for visiting our store. We hope to see you back soon!")
        break
    
    # Ask if user want to go back and perform other actions.
    input('\nReady to change to other actions. Just click enter. ')
    
    # Clear the screen
    for i in range(100):
        print('\n')
    
