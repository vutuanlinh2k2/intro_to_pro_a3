# a file for storing general functions that can be used in other files

# a function to validate the number input from users
def validate_input_number(input_message, min, max):
    # make the error message
    error_message = f'Your input is not valid. Please only enter a number between {str(min)} and {str(max)}.'
    
    # a loop to ask users to re enter the input if the required was not satisfied
    while True:
        # ask the to enter a number
        try:
            userInput = int(input(input_message)) 

        # if their input cannot be converted to a number, raise the error message and ask them try again      
        except ValueError:
            print(error_message)
            continue
        else:
            # if the number is bigger than the maximum or smaller than the minimum required, ask them to try again
            if userInput < min or userInput > max:
                print(error_message)
                continue
            
            return userInput 

# a function to validate the string input from users       
def validate_input_string(input_message, error_message, valid_strings):
    
    # a loop to ask users to re enter the input if the required was not satisfied
    while True:
        # ask the to enter a string
        userInput = input(input_message)
        
        # if the input is invalid, ask them to try again
        if userInput.lower() not in valid_strings:
            print(error_message)
            continue
        
        return userInput.lower()
            