import math


# import random


def yes_no(question):
    """check that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes (y) or no (n). \n")


def string_checker(question, num_letters, valid_ans_list):
    """"checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:
        response = input(question).lower()

        if response == "xxx":
            return response

        for item in valid_ans_list:

            if response == item:
                return item

            elif response == "tri":
                item = "triangle"
                return item

            elif response == "tra":
                item = "trapezium"
                return item

            elif response == item[:num_letters]:
                return item

            elif response == "t":

                option = yes_no("Default shape is triangle. Change to trapezium? ")

                if option == "yes":
                    setting = "trapezium"
                    return setting
                else:
                    setting = "triangle"
                    return setting

        print(f"Please choose an option from {valid_ans_list}\n")


def number_checker(question, exit_code=None, num_type=None):
    """checks if an integer is more than zero"""

    error = "Enter a number more than zero."
    change_to = float

    if num_type == "integer":
        error = "Enter an integer more than zero."
        change_to = int

    while True:
        response = input(question).lower()

        if response == exit_code:
            return str(response)

        try:
            # change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def formula_check(response, exit_code):
    """calculates the chosen shape by their formula"""

    if response == exit_code:
        return response

    perimeter = 0
    area = 0

    # will replace values with random.randint()
    # and phrase question later on
    if response == "circle":
        perimeter = math.pi * (a * 2)
        area = math.pi * (a ** 2)

    # perhaps have 3 different types of triangles aka
    # right-angled, no 3rd side triangle (for perimeter question),
    # 3 side triangles

    elif response == "triangle":
        triangle_sides = number_checker("Number of unknown sides: ")
        if triangle_sides == 1:
            area = 1 / 2 * a * b

    elif response == "rectangle":
        area = ((a ** 2) * (b ** 2))
        perimeter = (a * 2) + (b * 2)

    elif response == "square":
        area = a ** 2
        perimeter = a * 4

    elif response == "trapezium":
        area = ((a + b) / 2) * c
        perimeter = a + b + c + d

    if perimeter or area <= 0:
        print(f"The perimeter / area must be non-negative or not equal to 0, "
              f"please check your values.\n")

    return area, perimeter


# initialise variables

# lists
variables = []
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]

# math loop for all problems to solve

while True:
    # ask user for the shape
    shape = string_checker("What shape are you solving? ", 1, shape_list)

    # Explain it was something to do with for loop? Crazy, I know.
    for i in range(4):
        length = number_checker("Enter the length's value: ", "xxx")

        if length == "xxx":
            break

        # for testing purposes, include in debugging slide
        print("variables", variables)
        variables.append(length)

    n = len(variables)
    print(n)

    # if missing 4 sides, put in n variables as substitutes
    # solves code list error
    if len(variables) < 4:
        for variables in range(4 - n):
            variables.append(0)

    a, b, c, d = variables
    print(variables)

    # calculate the shape's area / perimeter
    formula = formula_check(shape, "xxx")
    print("you chose", shape, "\n")
