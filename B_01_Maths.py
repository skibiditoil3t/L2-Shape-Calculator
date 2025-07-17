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
    """Gives the instructions to users"""
    print("\n")
    print(make_statement("Instructions", "="))

    print('''
--- HOW TO ---
Welcome to the MHS Maths Shape Calculator!

To start, you'll be prompted to choose from 5 shapes:
circle, square, rectangle, triangle or trapezium.

You can enter the shape's first letter, first three letters, or full name.

Once you've chosen a shape, it's area formula will be printed 
and it'll show which variables belong to which side.
You must enter according to it's formula.

When it loops back to choosing another shape,
you can enter 'xxx' to view the shapes you've calculated and also see it 
on a file in your computer.

--- SETTINGS ---
't':
If you write 't', you'll be prompted to set either triangle or trapezium as 't'.
Once it's set, enter 'triangle' or 'trapezium' to overwrite what 't' defaults to.

(NOTE: You won't be prompted if you've entered triangle or trapezium previously!)

'round':
Change how many decimal places you round to from it's default of 2.
'0' is accepted if you want to round to the nearest whole number instead.

        ''')


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

        elif response == "round":
            round_to = number_checker("Round to: ")
            round_setting.insert(0, round_to)
            return "round"

        # iterates through every item in a list and checks
        # if it matches the user's response
        for i in valid_ans_list:
            if response == i or response == i[:num_letters] or response == i[:3]:
                return i

            elif response == "t":

                # Returns the shape set to 't' if it's already there
                if len(shape_setting) > 0:
                    setting = shape_setting[0]
                    return setting

                option = yes_no("\nDefault shape for 't' is triangle. Change to trapezium? ")

                setting = "triangle"

                if option == "yes":
                    setting = "trapezium"

                return setting

        print(f"Please choose an option from {valid_ans_list}\n")


def number_checker(question, num_type=None, exit_code=None):
    """Checks if the value given is greater than zero"""

    error = "Enter an integer greater than zero."
    change_to = int

    if num_type == "float":
        error = "Enter a number greater than zero."
        change_to = float

    while True:
        response = input(question).lower()

        if response == exit_code:
            return str(response)

        try:
            # change the response to a float and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            elif num_type == "round" and response == 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def formula_check(response, exit_code):
    """calculates the user's shape by the shape's according formula
        and outputs the results"""

    # initialise variables
    area = 0
    perimeter = 0
    results = f"Area: {area}\nPerimeter: {perimeter}"

    if response == exit_code:
        return response

    # match response with shape and calculate area (perimeter too if possible)
    if response == "circle":
        perimeter = math.pi * (a * 2)
        area = math.pi * (a ** 2)

    elif response == "triangle":

        # if 2nd side isn't 0, calculate a right-angled triangles area
        if b != 0:
            area = 1 / 2 * a * b
            perimeter = math.sqrt(a ** 2 + b ** 2)

            # if 3rd side isn't 0, calculate a scalene triangle's area
            if c != 0:
                s = (a + b + c) / 2

                try:
                    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                    perimeter = a + b + c

                # if 2 of the sides are smaller than 1 side, give user an error
                except ValueError:
                    minimum = [i for i in variables if 0 < i < max(variables)]
                    results = (f"Impossible Triangle: Value [{max(variables)}] is greater than"
                          f" the sum of the other 2 values {minimum}.")

        # If only one side is given, we only print out the error.
        else:
            results = "Invalid Triangle: Only one value given."

    elif response == "rectangle":
        area = a * b
        perimeter = (a * 2) + (b * 2)

    elif response == "square":
        area = a ** 2
        perimeter = a * 4

    # need to check which is height and the parallel sides
    elif response == "trapezium":
        area = ((a + b) / 2) * c
        if d > 0:
            perimeter = a + b + c + d

    # output area for shapes
    if area != 0:

        # rounding area and perimeter
        area = f'{area:.{round_setting[0]}f}'
        perimeter = f'{perimeter:.{round_setting[0]}f}'

        # PANDAS area
        all_shapes.append(response)
        all_area.append(area)
        all_perimeter.append(perimeter)

    if shape in shape_list:
        if shape == "triangle":
            if b != 0 and c == 0:
                perimeter = "N/A"
            else:
                if area == 0:
                    area = "N/A"
                    perimeter = "N/A"

        # If the 4th side isn't given in a trapezium,
        # the programme assumes the user only wants to solve for area.
        elif shape == "trapezium":
            if d <= 0:
                perimeter = "N/A"

        elif shape == "circle":
            results = f"Area: {area} \nCircumference: {perimeter}"
    print(f"\n{results}")

    return area, perimeter


def area_formula(response):

    if response == "square" or response == "circle":
        i = 1
        text_formula = "a\u00b2"

        if response == "circle":
            text_formula = " \u03c0 * a\u00b2"

    elif response == "rectangle":
        i = 2
        text_formula = "a * b"

    elif response == "triangle":
        i = 3
        text_formula = ("\U0000221As(s-a)(s-b)(s-c) "
                   "\n['s' is calculated after a, b and c are given].")

        sides = yes_no("Do you have 3 sides? ")

        if sides == "no":
            i = 2
            text_formula = "a * b / 2"

        shape_setting.insert(0, response)

    else:
        i = 4

        height = number_checker("Length of height ('xxx' if no height available): ",
                                "float", "xxx")

        text_formula = ("(a + b / 2) * c )  "
                        "\nSide 'd' is only to calculate perimeter.")

        if height == "xxx":
            i = 4
            text_formula = "(a + b / 2) * √[c² - ((b - a)² + c² - d² / (2 * (b - a))²]"

        shape_setting.insert(0, response)

    # gives user the area formula of the shape
    print(f"\nArea formula: {text_formula}\n")

    return i

# initialise variables
loop_ran = 0

# lists
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]
string_variables = ['a',  'b', 'c', 'd']
shape_setting = []
round_setting = [2]
all_shapes = []
all_area = []
all_perimeter = []

# PANDAS dictionary
shape_calc_dict = {
    "Shape": all_shapes,
    "Area": all_area,
    "Perimeter": all_perimeter,
}

# ask user if they want instructions
want_instructions = yes_no("Do you want instructions? ")

if want_instructions == "yes":
    instruction()

# math loop starts

while True:

    # initialise list
    variables = []

    # ask user for the shape
    shape = string_checker("\nWhat shape are you solving? ", 1, shape_list)

    if shape == "xxx":
        break
    elif shape == "round":
        continue
    print(shape)

    # 'n' is how many times we need to ask the user for the side / base / height of their shape
    n = area_formula(shape)
    loop_ran = 0

    # runs loop 'n' amount of times
    for item in range(n):
        length = number_checker(f"Length of Side {string_variables[0 + loop_ran]}: ", 'float', 'xxx')

        if length == "xxx":
            break

        variables.append(length)
        loop_ran += 1

    # checks how many variables the user has entered
    n = len(variables)

    # if not all 4 sides present, put in 'n' amount of zeros
    if n < 4:
        for item in range(4 - n):
            variables.append(0)

    a, b, c, d = variables

    # calculate the shape's area / perimeter
    formula = formula_check(shape, "xxx")

# Output area
if len(all_shapes) != 0:
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

    # printing area
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