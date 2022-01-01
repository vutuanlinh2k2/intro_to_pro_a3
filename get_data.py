from books import books_list

def get_books_data():
    """
    This function will convert data in txt file into py file
    :param: None
    :return: list of converted data (list)
    """
    books_data_dict = {}

    # Open and read the file that need to be converted
    with open('books.txt', "r") as books_data:
        for line in books_data:

            # Split each line into different pairs
            [id, name, quantity, average_rate, num_of_rates] = line.split(' | ')
            books_data_dict[int(id)] = {}
            books_data_dict[int(id)]["name"] = name
            books_data_dict[int(id)]["quantity"] = int(quantity)
            books_data_dict[int(id)]["num_of_rates"] = int(num_of_rates)

            # Convert the rating to float type (Keep the same if is N/A)
            try:
                books_data_dict[int(id)]["average_rate"] = float(average_rate)
            except ValueError:
                books_data_dict[int(id)]["average_rate"] = average_rate

    # Update the book database in the python file
    for book in books_list:
        book["quantity"] = books_data_dict[book["id"]]["quantity"]
        book["num_of_rates"] = books_data_dict[book["id"]]["num_of_rates"]
        book["average_rate"] = books_data_dict[book["id"]]["average_rate"]

    return books_list

def get_customers_data():
    """
    This function will upadte the data of customers to the text file
    :param: None
    :return: dictionary of customer data (dict)
    """
    customers_data_dict = {}

    # Open and read the file that need to be converted
    with open('customers.txt', "r") as customers_data:

        # Loop through each customer profile in the database
        for line in customers_data:
            [id, name, phone, email, address] = line.split(' | ')
            customers_data_dict[email] = {}
            customers_data_dict[email]["id"] = id
            customers_data_dict[email]["name"] = name
            customers_data_dict[email]["phone"] = phone
            customers_data_dict[email]["address"] = address.strip()

    return customers_data_dict
