from f10_vouchers import *
from utilities import *

# A function to help users selecting books they want to buy
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
        # Ask the users the id of the book they want to buy
        select_id = validate_input_number('Please enter the id of the book you want to buy: ', 0, len(books_list) - 1)
        
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
                print(f'There are {str(book["quantity"])} copies of this book left. Each copy cost {str(book["price"])}$.')
                
                # Ask for number of copies they want to buy
                number = validate_input_number('How many of them would you like to buy? ', 1, book["quantity"])

                # Update the books users have selected, the total price and the books database
                total += number * book["price"]
                books_info.append({
                    'id': book["id"],
                    'name': book['name'],
                    'number': number
                })
                book["quantity"] -= number
                
                # Give them the info of the book they just add to their order
                print(f'You have added {str(number)} copies of {book["name"]} to your order!')
                print(f'The total price of your order is now at {total}.')
                
                # Ask users if they want to buy more books
                buy_more = validate_input_string('Would you like to buy more books? ', "Please only type 'y'(yes) or 'n'(no)!", ['y', 'n'])
                
                # If they do not want to buy more, print the summary of all the book they have selected
                if buy_more.lower() == 'n':
                    print('You have bought:')
                    for book in books_info:
                        print(book['number'], ' copies of ', book['name'], ' .')
                    print(f'The total price of your order (before applying voucher) is {total}$.')
                    
                    return (total, books_info)
    
# A function to get users' information            
def getting_customer_info(customers_list):
    """
    This function will get the customer's information
    :param: The list of customers in our database (list)
    :return: the customer's email (str), name (str), phone number (str), and address (str)
    """
    email = input('Enter your email address: ')
    
    # Check if that email in the customers database
    for customer in customers_list:
        # If the email is in the customers database
        if customer["email"] == email:
            
            # Ask if they want to keep their information 
            change_info = validate_input_string(f'Hi {customer["name"]}. It appears that you have made previous order(s) in our store. Do you want to keep all your information the same (phone, address)? ', "Please only type 'y'(yes) or 'n'(no)!", ['y', 'n'])
            
            # If yes, finish the function
            if change_info.lower() == 'y':
                return (email, customer["name"], customer["phone"], customer["address"])
            
            # If no, ask them to update their information
            else:
                phone = input('Enter your new phone number: ')
                address = input('Enter your new address: ')
                
                # Update the customers database
                customer["phone"] = phone
                customer["address"] = address
                
                return (email, customer["name"], phone, address)
    
    # If the email is not in the customers database, ask them all the required information     
    name = input('Enter your name: ')
    phone = input('Enter your phone number: ')
    address = input('Enter your address: ')
    
    # Add new user to the customers database
    customers_list.append({
        "email": email,
        "phone": phone,
        "name": name,
        "address": address
    })
    
    f = open("customers.txt", "a")
    f.write(f"name:: {name} | phone:: {phone} | email:: {email} | address:: {address}\n")
    f.close()
    return (email, name, phone, address)

# The main function for placing order   
def place_order(books_list, customers_list):
    """
    This function will place the order of each customer
    :param: book_list: the list of books in our database (list)
    :param: customers_list: the list of customers in our database (list)
    :return: None
    """
    
    # Users select the books
    (total, books_info) = selecting_books(books_list)
    
    # Applying vouchers - Feature 10
    final_total = apply_voucher(total)
    
    # Getting user info
    (email, name, phone, address) =  getting_customer_info(customers_list)  
    
    # Print the summary of their order
    print('The summary of your order: ')
    for book in books_info:
        print(book['number'], 'copies of', book['name'], '.')
    print(f'The total price of your order is {final_total}$.')
    print('Your email: ', email)
    print('Your name: ', name)
    print('Your phone number: ', phone)
    print('Your address: ', address)
