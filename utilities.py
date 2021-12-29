# A file for storing general functions that can be used in other files

# A function to validate the number input from users
def validate_input_number(input_message, min, max):
    """
    This function will check the input number of customer if it is a number in the given range
    :param input_message: The input message that customer type (str)
    :param min: the minimum number (int)
    :param max: the maximum number (int)
    :return userInput: the validated input message
    """
    # Make the error message
    error_message = f'Your input is not valid. Please only enter a number between {str(min)} and {str(max)}.'
    
    # A loop to ask users to re enter the input if the required was not satisfied
    while True:
        # Ask the to enter a number
        try:
            userInput = int(input(input_message)) 

        # If their input cannot be converted to a number, raise the error message and ask them try again      
        except ValueError:
            print(error_message)
            continue
        else:
            # If the number is bigger than the maximum or smaller than the minimum required, ask them to try again
            if userInput < min or userInput > max:
                print(error_message)
                continue
            
            return userInput 

# A function to validate the string input from users       
def validate_input_string(input_message, error_message, valid_strings):
    """
    This function will check the input number of customer if it is a string that meets the requirement
    :param input_message: The input message that customer type (str)
    :param error_message: the error message to print (str)
    :param valid_strings: the list of valid strings (list)
    :return userInput: the validated input message
    """
    # A loop to ask users to re enter the input if the required was not satisfied
    while True:
        # Ask the to enter a string
        userInput = input(input_message)
        
        # If the input is invalid, ask them to try again
        if userInput.lower() not in valid_strings:
            print(error_message)
            continue
        
        return userInput.lower()
            