import math


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def instruction():
    print(make_statement("instructions", "="))

    print("instructions are here yo")
    return


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

        # iterates through every item in a list and checks
        # if it matches user's response
        for i in valid_ans_list:

            if response == i:
                return i

            elif response == "tri":
                i = "triangle"
                return i

            elif response == "tra":
                i = "trapezium"
                return i

            elif response == i[:num_letters]:
                return i

            elif response == "t":

                if response == "t" and len(shape_setting) > 0:
                    return shape_setting[0]

                option = yes_no("Default shape is triangle. Change to trapezium? ")

                if option == "yes":
                    setting = "trapezium"
                    shape_setting.append(setting)
                    return setting
                else:
                    setting = "triangle"
                    shape_setting.append(setting)
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
    """calculates the user's shape by the shape's according formula"""

    if response == exit_code or exit_code in variables:
        return response

    perimeter = 0
    area = 0
    hypotenuse = 0

    if response == "circle":
        perimeter = math.pi * (a * 2)
        area = math.pi * (a ** 2)

    # The type of Triangle calculated
    # is determined by how many sides the user gave
    # (i.e 2 sides = Right-angled, 3 sides = Heron's law needed)

    elif response == "triangle":

        if (a and b == float) and c + d == 0:
            print("Right-angled Triangle")
            area = 1 / 2 * a * b
            hypotenuse = math.sqrt(a ** 2 + b ** 2)
            perimeter = a + b + hypotenuse
        else:
            print("3 Sided Triangle")
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            perimeter = a + b + c

    elif response == "rectangle":
        area = ((a ** 2) * (b ** 2))
        perimeter = (a * 2) + (b * 2)

    elif response == "square":
        area = a ** 2
        perimeter = a * 4

    elif response == "trapezium":
        area = ((a + b) / 2) * c
        if d == float:
            perimeter = a + b + c + d
        else:
            perimeter = "N/A"

    elif perimeter or area <= 0:
        print(f"The perimeter / area must be non-negative or not equal to 0, "
              f"please check your values.\n")

    print("area:", area)
    print("perimeter:", perimeter)
    print("hypotenuse", hypotenuse)
    return area, perimeter, hypotenuse


# initialise variables
n = 0

# lists
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]
shape_setting = []

# Ask user if they want instructions
want_instructions = yes_no("Do you want instructions?")

if want_instructions == "yes":
    instruction()


# math loop for all problems to solve
while True:

    # empty list to put variables in, prevents 'too many unpacked' error
    variables = []

    # ask user for the shape
    shape = string_checker("What shape are you solving? ", 1, shape_list)
    print(shape)

    if shape == "circle" or "square":
        n = 1
    elif shape == "rectangle":
        n = 2
    elif shape == "triangle" or "trapezium":
        n = 3
    else:
        shape_setting = []
        continue

    print(n)
    # Runs loop 'n' amount of times
    for item in range(n):
        length = number_checker("Length of the side(s): ", 'xxx')
        variables.append(length)

    if shape == "trapezium" and n == "3":
        d = number_checker("4th Side?: ", 'xxx')

    # checks how many variables users put
    n = len(variables)

    # if not all 4 sides present, put in 'n' amount of zeros
    # prevents 'no variable to unpack' error
    if n < 4:
        for item in range(4 - n):
            variables.append(0)

    a, b, c, d = variables
    print(variables)

    # calculate the shape's area / perimeter
    formula = formula_check(shape, "xxx")
    print("you chose", shape, "\n")
    print(formula)
