from validate_input import validate_input_y_n

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
    
    applying = validate_input_y_n('Would you like to apply coupon? (y/n) ')
    
    if applying:
        while True:
            coupon_input = input('Apply coupon: ')
            for voucher_type in vouchers.keys():    # Loop through different types of voucher
                if coupon_input == voucher_type:
                    # Applying the voucher
                    new_price = initial_price * vouchers[coupon_input]
                    print('Voucher has been successfully applied!')
                    print(f"The total amount of money you have to pay is {new_price}")
            else:
                # If the user types in an invalid voucher
                try_again = validate_input_y_n('Invalid coupon! Would you like to try again? (y/n) ')
                if not try_again:
                    break
    else:
        new_price = initial_price            
    return new_price     
