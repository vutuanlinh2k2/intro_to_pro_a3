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
    :return: None
    """
    coupon_input = input('Apply coupon: ')
    for voucher_type in vouchers.keys():    # Loop through different types of voucher
        if coupon_input == voucher_type:
            # Applying the voucher
            new_price = initial_price * vouchers[coupon_input]
            print('Voucher has been successfully applied!')
            print(f"The total amount of money you have to pay is {new_price}")
            return new_price
    else:
        # If the user types in an invalid voucher
        print('Invalid coupon!')
