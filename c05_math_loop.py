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
    """checks that users enter the full word
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

                option = yes_no("\nDefault shape for 't' is triangle. Change to trapezium? ")

                if option == "yes":
                    setting = "trapezium"
                    shape_setting.insert(0, setting)
                    return setting
                else:
                    setting = "triangle"
                    shape_setting.insert(0, setting)
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
    # (2 sides given = Right-angled, 3 sides given = Heron's law)

    elif response == "triangle":
        if (a and b > 0) and c + d == 0:
            area = 1 / 2 * a * b
            hypotenuse = math.sqrt(a ** 2 + b ** 2)
        elif a+b+c > 0:
            s = (a + b + c) / 2
            try:
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                perimeter = a + b + c
            except ValueError:
                minimum = [i for i in variables if 0 < i < max(variables)]
                print(f"\nImpossible Triangle: length [{max(variables)}] is a greater than"
                      f" the sum of the other 2 lengths {minimum}")
                area = "N/A"
                perimeter = "N/A"
        else:
            print("Invalid Triangle, only one side given.")

    elif response == "rectangle":
        area = ((a ** 2) * (b ** 2))
        perimeter = (a * 2) + (b * 2)

    elif response == "square":
        area = a ** 2
        perimeter = a * 4

    elif response == "trapezium":
        area = ((a + b) / 2) * c
        if d > 0:
            perimeter = a + b + c + d
        else:
            perimeter = "N/A"


    if shape in shape_list:
        if perimeter or area == 0 or sum(variables) == 0:
            print(f"The area / perimeter must be non-negative or not equal to 0, "
              f"please check your values.\n")
        else:
            print("Area: ", area)
            print("Perimeter: ", perimeter)

    elif shape == "triangle" and (a+b > 0 and c+d == 0):
        print("Area:", area)
        print("Hypotenuse:", hypotenuse)

    return area, perimeter


# initialise variables
n = 0

# lists
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]
shape_setting = []

# Ask user if they want instructions
want_instructions = yes_no("Do you want instructions? ")

if want_instructions == "yes":
    instruction()

# math loop for all problems to solve
while True:

    # empty list to put variables in, prevents 'too many unpacked' error
    variables = []

    # ask user for the shape
    shape = string_checker("What shape are you solving? ", 1, shape_list)

    if shape == "xxx":
        continue

    # Runs loop 'n' amount of times
    for item in range(4):
        length = number_checker("Length of the side(s): ", 'xxx')
        if length == "xxx":
            break
        variables.append(length)

    # checks how many variables users put
    n = len(variables)

    # if not all 4 sides present, put in 'n' amount of zeros
    # prevents 'no variable to unpack' error
    if n < 4:
        for item in range(4 - n):
            variables.append(0)

    a, b, c, d = variables

    # calculate the shape's area / perimeter
    formula = formula_check(shape, "xxx")
