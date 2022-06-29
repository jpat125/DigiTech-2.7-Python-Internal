def validate_integer():    
    while True:
        try:
            input = int(input("input")) # Try to convert the input into a number
            break                    # Break out of the infinite loop if the conversion is successful
        except ValueError:       # Do this instead if the try block causes a ValueError
            print("Sorry, that is not an integer. Please try again.")

validate_integer()