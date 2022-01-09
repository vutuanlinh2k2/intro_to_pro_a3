from f10_vouchers import apply_voucher
from validate_input import validate_input_number, validate_input_y_n, validate_email, validate_phone
from get_data import get_books_data, get_customers_data
from update_data import update_book_quantity, add_new_customer, update_customer_address


# Feature 6: place order


def selecting_books(books_list):
    """
    This function will help the customer to place book order
    :param books_list: the list of books in our database (list)
    :return: None
    """
    # Define variables for tracking all the books user selected and the total price
    total = 0
    books_info = []

    # A loop allow users to select multiple books
    while True:
        # Ask users the id of the book they want to buy
        select_id = validate_input_number('Please enter the id of the book you want to buy: ', 1, len(books_list))

        # A loop to find the book users are looking for
        for book in books_list:
            # Found the book the users are looking for
            if book["id"] == int(select_id):

                # If no copies with this id left, ask them to select other books
                if book["quantity"] == 0:
                    print('Sorry, this book has been sold out. Please select another book instead.')
                    break

                # If there still copies with this id, provide users some info of the book
                print(f'You are adding the book {book["name"]} to your order.')
                print(
                    f'There are {str(book["quantity"])} copies of this book left. Each copy cost ${str(book["price"])}.')

                # Ask for number of copies they want to buy
                number = validate_input_number('How many of them would you like to buy? ', 1, book["quantity"])

                # Update the books users have selected, the total price and the books database
                total += number * book["price"]
                books_info.append({
                    'id': book["id"],
                    'name': book['name'],
                    'number': number
                })

                update_book_quantity(select_id, number)

                # Give them the info of the book they just add to their order
                print(f'You have added {str(number)} copies of {book["name"]} to your order!')
                print(f'The total price of your order is now at ${total}.')

                # Ask users if they want to buy more books
                buy_more = validate_input_y_n('Would you like to buy more books? (y/n) ')

                # If they do not want to buy more, print the summary of all the book they have selected
                if not buy_more:
                    print('You have bought:')
                    for book in books_info:
                        print(book['number'], ' copies of ', book['name'], ' .')
                    print(f'The total price of your order (before applying voucher) is ${total}.')

                    return total, books_info


# A function to get users' information            
def getting_customer_info(customers_list):
    """
    This function will get the customer's information
    :param: The list of customers in our database (list)
    :return: the customer's email (str), name (str), phone number (str), and address (str)
    """
    email = validate_email('Enter your email address: ')

    # If the email in the customers database   
    if email in customers_list:
        change_info = validate_input_y_n(
            f'Hi {customers_list[email]["name"]}. It appears that you have made previous order(s) in our store. Do '
            f'you want to keep your shipping address the same? (y/n) ')

        if change_info:  # If the customer want to keep the address the same
            return (
                email, customers_list[email]["name"], customers_list[email]["phone"], customers_list[email]["address"])
        else:  # If the customer want to change to a new address
            address = input('Enter your new address: ')
            update_customer_address(email, address)
            return email, customers_list[email]["name"], customers_list[email]["phone"], address

    # If the email is not in the customers database, ask them all the required information     
    name = input('Enter your name: ')
    phone = validate_phone('Enter your phone number: ')
    address = input('Enter your address: ')

    add_new_customer(name, phone, email, address)
    return email, name, phone, address


# The main function for placing order
def place_order():
    """
    This function will place the order of each customer
    :param: None
    :return: None
    """
    books_list = get_books_data()
    customers_list = get_customers_data()

    # Users select the books
    (total, books_info) = selecting_books(books_list)

    # Applying vouchers - Feature 10
    final_total = apply_voucher(total)

    # Getting user info
    (email, name, phone, address) = getting_customer_info(customers_list)

    # Print the summary of their order
    print('The summary of your order: ')
    for book in books_info:
        print(book['number'], 'copies of', book['name'])
    print(f'The total price of your order is {final_total}$.')
    print('Your email: ', email)
    print('Your name: ', name)
    print('Your phone number: ', phone)
    print('Your address: ', address)
