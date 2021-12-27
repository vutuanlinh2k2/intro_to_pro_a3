# Feature 2: List all items' information:
def book_info(books_list):
    book_id = input("Enter the ID of the book that you want to see: ")
    selected_book = books_list[int(book_id)]
    print(selected_book['name'], 'written by', selected_book['author'])
    print('Genre:', selected_book['genre'], '| Number of pages:', selected_book['pages'])
    print(selected_book['description'])
    print('Price: $', selected_book['price'], '| Quantity:', selected_book['quantity'])
    print('Avarage ratings:', selected_book['average_rate'], '| Number of rates: ', selected_book['num_of_rates'])