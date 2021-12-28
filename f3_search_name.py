# Feature 3: Search book by name
def name_search(books_list):
    """
    This function will help the customer to search a book by typing its name
    :param books_list: the list of book in our database
    :return: None
    """
    search_name = input("Enter the name of the book you want to search: ")
    num = 0
    for book in books_list:
        if search_name.lower() in book["name"].lower():
            print("Id:", book["id"], "| Name:", book["name"], "| Author:", book["author"], "| Quantity:", book["quantity"])
            num += 1

    # In case the chosen book's name is not in our store's database
    if num == 0:
        print("We can't find any book with that name!")