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
                k, v = component.split("::")
                data_dct[k.strip()] = v.strip()

            # Add dictionaries into a list
            data_lst.append(data_dct)

    return data_lst











