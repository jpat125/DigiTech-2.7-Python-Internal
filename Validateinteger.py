def validate_integer(prompt):
    while True:
        try:
            int_input = int(input(prompt))
            return int_input
        except ValueError:
            print("Please input a floating point number ")
