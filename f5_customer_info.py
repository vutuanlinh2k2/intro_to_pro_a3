from get_data import get_customers_data

# Feature 5: List all info of a specific customer
def customer_info():
    """
    This function will list all information of a specific customer using their email address to distinguish
    :param: None
    :return: None
    """
    customers_data = get_customers_data()
    email = input('Please enter an email address: ')
    if email in customers_data:
        print('Customer id:', customers_data[email]["id"])
        print("Customer name:", customers_data[email]['name'])
        print("Phone:", customers_data[email]['phone'])
        print("Email:", email)
        print("Address:", customers_data[email]['address'])
    else:
        print('Sorry we cannot find customer with that email!')