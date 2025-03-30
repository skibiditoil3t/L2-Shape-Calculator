import math
import random


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


def number_checker(question, num_type, exit_code=None):
    """"checks if an integer is more than zero"""

    if num_type == "integer":
        error = "enter an integer more than zero bruh"
        change_to = int
    else:
        error = "enter a number mo' than zero bruh"
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


def formula_check(response, exit_code):
    """calculates the chosen shape by their formula"""

    # initialise variables
    a = random.triangular(0, 10)
    b = random.triangular(0, 10)
    c = random.triangular(0, 10)
    d = random.triangular(0, 10)
    perimeter = 0
    area = 0

    if response == exit_code:
        return response

    # will replace values with random.randint()
    # and phrase question later on
    if response == "circle":
        perimeter = math.pi * (a * 2)
        area = math.pi * (a ** 2)

    # perhaps have 3 different types of triangles aka
    # right-angled, no 3rd side triangle (for perimeter question),
    # 3 side triangles

    elif response == "triangle":
        area = 1 / 2 * a * b
        perimeter = a + b + c

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
        print(f"The perimeter / area must be non-negative, please check your values.")

    return area, perimeter


# initialise variables
variables = []
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]

# math loop for all problems to solve

while True:
    # ask user for the shape
    shape = string_checker("What shape are you solving? ", 1, shape_list)

    # might implement solving for unknowns
    # I is so the loop can run
    i = 0
    solving_for = number_checker("How many sides do you know for the shape? ", "integer")

    while i != solving_for:
        i += 1
        value = number_checker("Enter your value: ", "float")
        variables.append(value)

        # prints are for testing purposes
        print(value)
        print(i)
        print(solving_for)

    print("loop is finished")

    # calculate the shape's area / perimeter
    formula = formula_check(shape, "xxx")
