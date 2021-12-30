from books import *

def read_data(data_file):
    """
    This function will convert data in txt file into py file
    :param data_file: name of txt file (str)
    :return: list of converted data (list)
    """
    data_lst = []

    # Open and read the file that need to be converted
    with open(data_file, "r") as data:
        for line in data:
            data_dct = {}

            # Split each line into different pairs
            components = line.split('|')

            # Split each pair and add key and value of each pair into a dictionary
            for component in components:
                key, value = component.split("::")
                
                try:
                    number_value = int(value) 

                except ValueError:
                    data_dct[key.strip()] = value.strip()
                else:
                    data_dct[key.strip()] = number_value

            # Add dictionaries into a list
            data_lst.append(data_dct)

    return data_lst

print(read_data('books.txt'))











