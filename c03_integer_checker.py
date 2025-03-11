def number_checker(question, num_type, exit_code=None):
    """checks if an integer is more tan zero"""

    if num_type == "integer":
        error = "Enter an integer more than 0"
        change_to = int
    else:
        error = "Enter a real positive number more than 0"
        change_to = float

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            # change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


my_int = number_checker("1+1? ", "integer", '')

if my_int == "":
    print("you have chosen infinite mode.")
else:
    print(f"you've chosen {my_int}")
