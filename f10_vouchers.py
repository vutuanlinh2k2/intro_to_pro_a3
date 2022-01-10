from validate_input import validate_input_y_n

# Feature 10: Applying voucher


# Declare list of vouchers with discount rate for each one
vouchers = {
    "SALE1111": 0.8,
    "SALE1212": 0.7,
    'LOVE101': 0.5,
    'ILOVEBOOKS': 0.3
}


def apply_voucher(initial_price):
    """
    This function will help the customer to apply voucher
    :param initial_price: the initial price of that order (float)
    :return: the final price (float)
    """
    # Ask customers to choose to apply voucher or not
    applying = validate_input_y_n('\nWould you like to apply a voucher? (y/n) ')
    
    # If customers choose to apply voucher
    if applying:     
        while True:
            voucher_input = input('Apply voucher: ')

            # Loop through different types of voucher
            for voucher_type in vouchers.keys():               
                if voucher_input == voucher_type:
                    # Applying the voucher
                    new_price = round(initial_price * vouchers[voucher_input], 2)
                    print('\nVoucher has been successfully applied!')
                    print(f"The total amount of money you have to pay is {new_price}")
                    return new_price
            else:  # If the user types in an invalid voucher
                try_again = validate_input_y_n('\nInvalid voucher! Would you like to try again? (y/n) ')
                if not try_again:   # Quit if customers do not want to apply voucher anymore
                    break

    # Price remains the same if no voucher was applied
    return initial_price 

