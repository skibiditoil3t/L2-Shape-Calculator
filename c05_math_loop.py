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

            if response == "tri":
                item = "triangle"
                return item

            if response == "tra":
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

    error = "oops - please enter an integer more than zero"
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


def math_loop(response, exit_code):
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
        perimeter = math.pi * (a*2)
        area = math.pi * (a ** 2)

    # perhaps have 3 different types of triangles aka
    # right-angled, no 3rd side triangle (for perimeter question),
    # 3 side triangles

    elif response == "triangle":
        area = 1 / 2 * a * b
        perimeter = a + b + c

    elif response == "rectangle":
        area = ((a ** 2) * (b ** 2))

    elif response == "square":
        area = 0 ** 2
        perimeter = a + b + c + d

    elif response == "trapezium":
        area = ((a + b) / 2) * c
        perimeter = a + b + c + d

    mode = yes_no("Default to solving for Area, change to Perimeter? ")
    if mode == "yes":
        mode = perimeter
    else:
        mode = area

    question = number_checker(f"if {shape} = {mode}, what is {a}?",)


shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]

while True:
    shape = string_checker("What shape are you solving? ", 1, shape_list)
    formula = math_loop(shape, "xxx")
    print(formula)
