def validate_input_number(input_message, error_message, max):
    while True:
        try:
            userInput = int(input(input_message))       
        except ValueError:
            print(error_message)
            continue
        else:
            if userInput < 0 or userInput > max:
                print(error_message)
                continue
            return userInput 
        
def validate_input_string(input_message, error_message, valid_strings):
    while True:
        userInput = input(input_message)
        if userInput.lower() not in valid_strings:
            print(error_message)
            continue
        return userInput.lower()
            