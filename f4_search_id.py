# Feature 4: Search book by Id
def id_search(books_list):
    """
    This function will help the customer to search a book by typing its ID
    :param books_list: the list of book in our database
    :return: None
    """
    search_id = input("Enter the id of the book you want to search: ")
    num = 0
    for book in books_list:
        if book["id"] == int(search_id):
            print("Id:", book["id"], "| Name:", book["name"], "| Author:", book["author"], "| Quantity:", book["quantity"])
            num += 1

    # In case the chosen book's id is not in our store's database
    if num == 0:
        print("We can't find any book with that id")