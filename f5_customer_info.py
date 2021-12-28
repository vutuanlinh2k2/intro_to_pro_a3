# Feature 5: List all info of a specific customer
def customer_info(customers_list):
    """
    This function will list all information of a specific customer using their email address to distinguish
    :param customers_list: the list of customer in our database
    :return: None
    """
    email = input('Please enter an email address: ')
    for customer in customers_list:
        if customer["email"] == email:
            print("Customer id:", customer['id'])
            print("Customer name:", customer['name'])
            print("Phone:", customer['phone'])
            print("Email:", customer['email'])
            print("Address:", customer['address'])
            break
    else:
        print('We have no customer with that email!')