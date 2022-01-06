def update_book_rate(book_id, rate):
    """
    This function will upadte the data of customers to the text file
    :param book_id: the id of chosen book (int)
    :param rate: the rating customer assess (int)
    :return: None
    """

    # Open the text file in reading mode.
    with open('books.txt', "r") as books_data:  
        lines = books_data.readlines()

    # Open the text file in writing mode.
    with open('books.txt', "w") as books_data:

        for line in lines:  # Loop through each line in the text file (each line represents a customer profile).
            [id, name, quantity, average_rate, num_of_rates] = line.split(' | ')    # Identify each category of a customer profile.
            
            if book_id == int(id):

                if average_rate == 'N/A':   # When there is no rating for the chosen book.
                    average_rate = str(round(float(rate),1))
                else:   # When there are already ratings for the chosen book.
                    average_rate = str(round((float(average_rate) * int(num_of_rates) + rate) / (int(num_of_rates) + 1),1))

                # Update the rating of the chosen book.
                num_of_rates = str(int(num_of_rates) + 1)   
                updated_book_line = ' | '.join([id, name, quantity, average_rate, num_of_rates]) + '\n'
                books_data.write(updated_book_line)

                print('Thank you for rating this book!')
                print('The current average rate for this book is', average_rate)

            else:
                books_data.write(line)  # Write the same line if it is not the book customer choose.

                
def update_book_quantity(book_id, bought):
    """
    This function will upadte the quantity of books to the text file
    :param book_id: the id of chosen book (int)
    :param bought: the number of books are bought (int)
    :return: None
    """
    # Open the text file in reading mode.
    with open('books.txt', "r") as books_data:
        lines = books_data.readlines()

    # Open the text file in writing mode.
    with open('books.txt', "w") as books_data:

        # Loop through each line in the text file (each line represents a specific book status).
        for line in lines:
            [id, name, quantity, average_rate, num_of_rates] = line.split(' | ')

            # Update the quantity of books in the text file.
            if book_id == int(id):
                quantity = str(int(quantity) - bought)
                updated_book_line = ' | '.join([id, name, quantity, average_rate, num_of_rates])
                books_data.write(updated_book_line)
            else:
                books_data.write(line)


def add_new_customer(name, phone, email, address):
    """
    This function will add the profile of customers to the text file
    :param name: the new customer's name (str)
    :param email: the new customer's email (str)
    :param phone: the new customer's phone number (str)
    :param address: the new customer's address (str)
    :return: None
    """
    # Calculate the number of customers in the database.
    num_customers = len(open('customers.txt').readlines())

    # Open the text file in appending mode.
    with open('customers.txt', "a") as customers_data:
        
        # Add the new customer profile.
        new_customer_id = str(num_customers + 1)
        new_customers_line = ' | '.join([new_customer_id, name, phone, email, address]) + '\n'
        customers_data.write(new_customers_line)
    
        
def update_customer_address(customer_email, new_address):
    """
    This function will upadte the customers' address to the text file
    :param customer_email: the customer's email (str)
    :param new_address: the customer's new address (str)
    :return: None
    """
    # Open the text file in reading mode.
    with open('customers.txt', "r") as customers_data:
        lines = customers_data.readlines()
    
    # Open the text file in writing mode.
    with open('customers.txt', "w") as customers_data:

        # Loop through each line in the text file (each line represents a customer profile).
        for line in lines:
            [id, name, phone, email, _] = line.split(' | ')

            # Update the customer profile.
            if customer_email == email:
                updated_customer_line = ' | '.join([id, name, phone, email, new_address]) + '\n'
                customers_data.write(updated_customer_line)
            else:
                customers_data.write(line)
                
