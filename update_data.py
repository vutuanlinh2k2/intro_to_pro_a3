def update_book_rate(book_id, rate):
    with open('books.txt', "r") as books_data:
        lines = books_data.readlines()
    with open('books.txt', "w") as books_data:
        for line in lines:
            [id, name, quantity, average_rate, num_of_rates] = line.split(' | ')
            if book_id == int(id):
                if average_rate == 'N/A':
                    average_rate = str(rate)
                else:
                    average_rate = str((float(average_rate) * int(num_of_rates) + rate) / (int(num_of_rates) + 1))
                num_of_rates = str(int(num_of_rates) + 1)
                updated_book_line = ' | '.join([id, name, quantity, average_rate, num_of_rates]) + '\n'
                books_data.write(updated_book_line)
                print('Thank you for rating this book!')
                print('The current average rate for this book is', average_rate)
            else:
                books_data.write(line)

                
def update_book_quantity(book_id, bought):
    with open('books.txt', "r") as books_data:
        lines = books_data.readlines()
    with open('books.txt', "w") as books_data:
        for line in lines:
            [id, name, quantity, average_rate, num_of_rates] = line.split(' | ')
            if book_id == int(id):
                quantity = str(int(quantity) - bought)
                updated_book_line = ' | '.join([id, name, quantity, average_rate, num_of_rates])
                books_data.write(updated_book_line)
            else:
                books_data.write(line)


def add_new_customer(name, phone, email, address):
    num_customers = len(open('customers.txt').readlines())
    with open('customers.txt', "a") as customers_data:
        new_customer_id = str(num_customers + 1)
        new_customers_line = ' | '.join([new_customer_id, name, phone, email, address]) + '\n'
        customers_data.write(new_customers_line)
    
        
def update_customer_address(customer_email, new_address):
    with open('customers.txt', "r") as customers_data:
        lines = customers_data.readlines()
    with open('customers.txt', "w") as customers_data:
        for line in lines:
            [id, name, phone, email, _] = line.split(' | ')
            if customer_email == email:
                updated_customer_line = ' | '.join([id, name, phone, email, new_address]) + '\n'
                customers_data.write(updated_customer_line)
            else:
                customers_data.write(line)
                
