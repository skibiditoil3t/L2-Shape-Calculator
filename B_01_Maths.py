import math
import pandas
from tabulate import tabulate
from datetime import datetime

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
                if response == "triangle" or response == "trapezium":
                    shape_setting.insert(0, i)
                return i

            elif response == "tri":
                i = "triangle"
                shape_setting.insert(0, i)
                return i

            elif response == "tra":
                i = "trapezium"
                shape_setting.insert(0, i)
                return i

            elif response == i[:num_letters]:
                return i

            elif response == "t":

                # Returns the setting
                if response == "t" and len(shape_setting) > 0:
                    return shape_setting[0]

                option = yes_no("\nDefault shape for 't' is triangle. Change to trapezium? ")

                if option == "yes":
                    setting = "trapezium"
                else:
                    setting = "triangle"

                shape_setting.insert(0, setting)
                return setting

        print(f"Please choose an option from {valid_ans_list}\n")


def number_checker(question, exit_code=None):
    """checks if an integer is more than zero"""

    error = "Enter a number more than zero."
    change_to = float

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

    # Match response with shape and calculate accordingly
    if response == "circle":
        perimeter = math.pi * (a * 2)
        area = math.pi * (a ** 2)

    # The type of Triangle calculated
    # is determined by how many sides the user gave
    # (2 sides given = Right-angled, 3 sides given = Heron's law)

    elif response == "triangle":
        # checks if 2 variables > 0 are given and variable 'c' = 0
        # assumes it's a right-angled triangle
        if (a > 0 and b > 0) and c == 0:
            area = 1 / 2 * a * b
            perimeter = math.sqrt(a ** 2 + b ** 2)

        # checks if user has entered 3 variables and the 2nd one isn't 0
        elif a+b+c > 0 and b != 0:
            s = (a + b + c) / 2
            try:
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                perimeter = a + b + c

            # if 2 of the sides are smaller than 1 side, give user an error
            except ValueError:
                minimum = [i for i in variables if 0 < i < max(variables)]
                print(f"\nImpossible Triangle: Value [{max(variables)}] is greater than"
                      f" the sum of the other 2 values {minimum}.")
                area = 0
                perimeter = 0
        else:
            # If only one side is given, we only print out the error.
            print("Invalid Triangle: Only one value given.")

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
            perimeter = 0

    if shape == "triangle" and ((a > 0 and b > 0) and c+d == 0):
        print("\nArea:", area)
        print("Hypotenuse:", perimeter)

    # If the 4th side isn't present in a trapezium,
    # the programme assumes the user only wants to solve for area.
    elif shape == "trapezium" and (a > 0 and b > 0 and c > 0 and d == 0):
        print("\nArea:", area)
        perimeter = "N/A"
        print("Perimeter:", perimeter)

    elif shape == "circle":
        print("\nArea:", area)
        print("Circumference:", perimeter)

    elif shape in shape_list:
        if perimeter <= 0 or area <= 0 or sum(variables) <= 0:
            print(f"The area / perimeter must be non-negative or not equal to 0, "
              f"please check your values.")
            area = "N/A"
            perimeter = "N/A"
        else:
            print("\nArea: ", area)
            print("Perimeter: ", perimeter)


    all_shapes.append(response)
    all_area.append(area)
    all_perimeter.append(perimeter)

    return area, perimeter


# initialise variables
n = 0
formula = 0
loop_ran = 0

# lists
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]
shape_setting = []

# dictionaries to hold
all_shapes = []
all_area = []
all_perimeter = []

shape_calc_dict = {
    "Shape": all_shapes,
    "Area": all_area,
    "Perimeter": all_perimeter,
}

# Ask user if they want instructions
want_instructions = yes_no("Do you want instructions? ")

if want_instructions == "yes":
    instruction()

# math loop for all problems to solve
while True:

    # empty list to put variables in, prevents 'too many unpacked' error
    variables = []

    # ask user for the shape
    shape = string_checker("\nWhat shape are you solving? ", 1, shape_list)

    # 'n' is how many times we need to ask in order to calculate area & perimeter
    if shape == "xxx":
        break
    elif shape == "square" or shape == "circle":
        n = 1
    elif shape == "rectangle":
        n = 2
    elif shape == "triangle":
        n = 3
    elif shape == "trapezium":
        n = 4

    # Runs loop 'n' amount of times
    for item in range(n):
        length = number_checker("Length of the side / base / height: ", 'xxx')
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
    loop_ran += 1

if shape == "xxx" and loop_ran > 0:
    # prepare date for proper file format
    today = datetime.today()

    # get day / month / year as individual strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    # headings / strings
    main_heading_string = make_statement(f"Math Calculator, {day} / {month} / {year}", "=")

    shape_calc_frame = pandas.DataFrame(shape_calc_dict)
    shape_calc_string = tabulate(shape_calc_frame, headers='keys',
                                 tablefmt='psql', showindex=False)

    # list of strings to be outputted / written to file
    to_write = ["", main_heading_string, "\n", shape_calc_string]
    # print area
    print()
    for item in to_write:
        print(item)

    # create file to hold data (add .txt extension)
    # prepare date for proper file format

    file_name = f"Math_Calculator_{year}_{month}_{day}"
    write_to = "{}.txt".format(file_name)

    text_file = open(write_to, "w+")

    # write the item to file
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")
else:
    print("No shape was calculated.")