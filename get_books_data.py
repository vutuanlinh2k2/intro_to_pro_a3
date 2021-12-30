from books import books_list


def get_books_data():
    """
    This function will convert data in txt file into py file
    :param data_file: name of txt file (str)
    :return: list of converted data (list)
    """
    data_dict = {}

    # Open and read the file that need to be converted
    with open('books.txt', "r") as data:
        for line in data:

            # Split each line into different pairs
            [id, name, quantity, average_rate,
                num_of_rates] = line.split(' | ')
            data_dict[int(id)] = {}
            data_dict[int(id)]["name"] = name
            data_dict[int(id)]["quantity"] = int(quantity)
            data_dict[int(id)]["num_of_rates"] = int(num_of_rates)

            try:
                data_dict[int(id)]["average_rate"] = float(average_rate)
            except ValueError:
                data_dict[int(id)]["average_rate"] = average_rate

    for book in books_list:
        book["quantity"] = data_dict[book["id"]]["quantity"]
        book["num_of_rates"] = data_dict[book["id"]]["num_of_rates"]
        book["average_rate"] = data_dict[book["id"]]["average_rate"]

    return books_list
