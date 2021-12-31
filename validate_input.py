# A file for storing general functions that can be used in other files

# A function to validate the number input from users
def validate_input_number(input_message, min, max):
    """
    This function will check the input number of customer if it is a number in the given range
    :param input_message: The input message that customer type (str)
    :param min: the minimum number (int)
    :param max: the maximum number (int)
    :return user_input: the validated input message (int)
    """
    # Make the error message
    error_message = f'Your input is not valid. Please only enter a number between {str(min)} and {str(max)}.'
    
    # A loop to ask users to re enter the input if the required was not satisfied
    while True:
        # Ask the to enter a number
        try:
            user_input = int(input(input_message)) 

        # If their input cannot be converted to a number, raise the error message and ask them try again      
        except ValueError:
            print(error_message)
            continue
        else:
            # If the number is bigger than the maximum or smaller than the minimum required, ask them to try again
            if user_input < min or user_input > max:
                print(error_message)
                continue
            
            return user_input 

# A function to validate the string input from users       
def validate_input_string(input_message, error_message, valid_strings):
    """
    This function will check the input number of customer if it is a string that meets the requirement
    :param input_message: The input message that customer type (str)
    :param error_message: the error message to print (str)
    :param valid_strings: the list of valid strings (list)
    :return user_input: the validated input message (str)
    """
    # A loop to ask users to re enter the input if the required was not satisfied
    while True:
        # Ask the to enter a string
        user_input = input(input_message)
        
        # If the input is invalid, ask them to try again
        if user_input.lower() not in valid_strings:
            print(error_message)
            continue
        
        return user_input.lower()
    
def validate_input_y_n(input_message):
    """
    This function will check the input number of customer if it is a string that meets the requirement
    :param input_message: The input message that customer type (str)
    :return: True/False
    """
    # A loop to ask users to re enter the input if the required was not satisfied
    while True:
        # Ask the to enter a string
        user_input = input(input_message)
        
        # If the input is invalid, ask them to try again
        if user_input.lower() not in ['y', 'n']:
            print("Please only type 'y' (yes) or 'n'(no)!")
            continue
        
        if user_input.lower() == 'y':
            return True
        
        return False
        
        
            