import math


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


def formula_check(response, exit_code):
    """calculates the chosen shape by their formula"""
    area = 0
    perimeter = 0

    if response == exit_code:
        return response

    # will replace values with random.randint()
    # and phrase question later on
    if response == "circle":
        radius = 0
        perimeter = 2 * math.pi * radius
        area = math.pi * (radius ** 2)

    # perhaps have 3 different types of triangles aka
    # right-angled, no 3rd side triangle (for perimeter question),
    # 3 side triangles

    elif response == "triangle":
        base = 0
        height = 0
        side = 0
        perimeter = base + height + side
        area = 1 / 2 * base * height

    elif response == "rectangle":
        length = 0
        width = 0
        perimeter = (length + width) * 2
        area = length * width

    elif response == "square":
        a = 0
        perimeter = a * 4
        area = 0 ** 2

    elif response == "trapezium":
        base_2 = 0
        base = 0
        height = 0
        perimeter = 0
        area = ((base_2 + base) / 2) * height

    return area, perimeter


# initialise variables

shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]

while True:
    shape = string_checker("What shape are you solving? ", 1, shape_list)
    formula = formula_check(shape, "xxx")
