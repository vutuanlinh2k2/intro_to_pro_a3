# A file for storing general functions that can be used in other files.


# Import regular expression module.
import re   


# A function to validate the number input from users.
def validate_input_number(input_message, min, max):
    """
    This function will check the input number of customer if it is a number in the given range
    :param input_message: The input message to ask customers (str)
    :param min: the minimum number (int)
    :param max: the maximum number (int)
    :return user_input: the validated input message (int)
    """
    # Make the error message.
    error_message = f'Your input is not valid. Please only enter a number between {str(min)} and {str(max)}.'
    
    # A loop to ask users to re enter the input if the required was not satisfied.
    while True:
        # Ask the to enter a number.
        try:
            user_input = int(input(input_message)) 

        # If their input cannot be converted to a number, raise the error message and ask them try again.      
        except ValueError:
            print(error_message)
            continue
        else:
            # If the number is bigger than the maximum or smaller than the minimum required, ask them to try again.
            if user_input < min or user_input > max:
                print(error_message)
                continue
            
            return user_input 

# A function to validate the string input from users.       
def validate_input_string(input_message, error_message, valid_strings):
    """
    This function will check the input number of customer if it is a string that meets the requirement
    :param input_message: The input message to ask customers (str)
    :param error_message: the error message to print (str)
    :param valid_strings: the list of valid strings (list)
    :return user_input: the validated input message (str)
    """
    # A loop to ask users to re enter the input if the required was not satisfied.
    while True:
        # Ask the to enter a string.
        user_input = input(input_message)
        
        # If the input is invalid, ask them to try again.
        if user_input.lower() not in valid_strings:
            print(error_message)
            continue
        
        return user_input.lower()
    
def validate_input_y_n(input_message):
    """
    This function will check the input number of customer if it is a string that meets the requirement
    :param input_message: The input message to ask customers (str)
    :return: True/False
    """
    # A loop to ask users to re enter the input if the required was not satisfied.
    while True:
        # Ask the to enter a string.
        user_input = input(input_message)
        
        # If the input is invalid, ask them to try again.
        if user_input.lower() not in ['y', 'n']:
            print("Please only type 'y' (yes) or 'n'(no)!")
            continue
        
        # Return True/False based on the input.
        if user_input.lower() == 'y':
            return True
        
        return False

def validate_email(input_message):
    """
    This function will check if the input has email account format
    :param input_message: The input message to ask customers (str)
    :return: the validated email account (str)
    """
    while True:
        email_input = input(input_message)

        # The email account must have exactly 1 "@" sign and 1 "." (dot) after that which represents the email domain.
        # Regular expression is used to check if the input satisfíes these above requirements.
        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email_input):
            return email_input
        else:
            print("Please enter a valid email address")
            continue

def validate_phone(input_message):
    """
    This function will check if the input has Vietnamese phone number format
    :param input_message: The input message to ask customers (str)
    :return: the validated phone number (str)
    """
    while True:
        phone_input = input(input_message)

        # A valid Vietnamese phone number must start with either 01, 03, 05, 07, 08 or 09.
        # If it starts with 01, the third number must be either 2, 6, 8 or 9.
        if re.fullmatch(r"(84|0[3|5|7|8|9])+([0-9]{8})\b", phone_input):
            return phone_input
        else:
            print("Please enter a valid Vietnamese phone number")
            continue

        
            