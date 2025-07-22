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
    print(make_statement("Instructions", "="))

    print('''
--- HOW TO ---
Welcome to the MHS Maths Shape Calculator!

To start, you'll be prompted to choose from 5 shapes:
circle, square, rectangle, triangle or trapezium.

You can enter the shape's first letter, first three letters, or full name.

Once you've chosen a shape, it's area formula will be shown
and you must enter the variables according to that formula.

When it loops back to choosing another shape,
you can enter 'xxx' to view the shapes you've calculated and also see it 
on a file in your computer.

--- SETTINGS ---
't':
If you write 't', you'll be prompted to set either triangle or trapezium as 't'.
Entering 'triangle' or 'trapezium' will overwrite what 't' defaults to.

'round':
Change how many decimal places you round to from it's default of 0.
Don't change this if you're calculating with whole numbers.
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
                    return shape_setting[0]

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


def formula_check(response):
    """Checks the user's chosen shape and gives a formula to show
    where users should enter their side / base / height values"""

    additional_info = ""

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
        text_formula = "\U0000221As(s-a)(s-b)(s-c) "
        additional_info = "\n['s' is calculated after a, b and c are given]."

        sides = yes_no("Do you have 3 sides? ")

        if sides == "no":
            i = 2
            text_formula = "a * b / 2"
            additional_info = ""

        shape_setting.insert(0, response)

    else:
        i = 4

        h = yes_no("Do you have height? ")

        text_formula = "(a + b / 2) * Height"
        additional_info = ("\na = shorter base, b = larger base, c & d = legs"
                           " Height is calculated after giving 2 variables.")

        if h == "no":
            additional_info = ("\na = shorter base, b = larger base, c and d = legs"
                               "All sides are required to calculate the area.")

        height.insert(0, h)
        shape_setting.insert(0, response)

    # print the shape's area formula
    print("")
    print(make_statement(f"Area Formula: {text_formula} ", "="))
    print(additional_info, "\n")

    return i


def shape_formula(response):
    """Calculates the user's shape by the shape's according formula
        and outputs the results"""

    # initialise variables
    shape_area = 0
    shape_perimeter = 0
    h = 0

    if response == "xxx":
        return response

    # match response with shape and calculate the area and perimeter
    if response == "circle":
        shape_area = math.pi * (a ** 2)
        shape_perimeter = math.pi * (a * 2)

    elif response == "triangle":
        shape_area = 1 / 2 * a * b

        # if loop was ran 3 times, calculate the triangle using Heron's law
        if loop_ran == 3:
            s = (a + b + c) / 2

            try:
                shape_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                shape_perimeter = a + b + c

            except ValueError:
                shape_area = 0
                shape_perimeter = 0

        if shape_area < 0:
            shape_perimeter = 0
            pass

    elif response == "rectangle":
        shape_area = a * b
        shape_perimeter = (a * 2) + (b * 2)

    elif response == "square":
        shape_area = a ** 2
        shape_perimeter = a * 4

    elif response == "trapezium":

        # calculates height if it's not present
        if height[0] == "no":
            try:
                e = b-a
                h = math.sqrt(e ** 2 - (c ** 2))
            except ValueError:
                h = 0

        # checks if 'xxx' wasn't entered as the first variable, then prompts user for height
        elif isinstance(variables[0], str):
            h = number_checker("Length of Height: ", "float")

        shape_area = (a + b) / 2 * h

        # checks if both bases are the same and makes area = 0
        if a == b:
            shape_area = 0
        elif c and d > 0:
            shape_perimeter = a + b + c + d

    return shape_area, shape_perimeter


# lists
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]
string_variables = ['a', 'b', 'c', 'd']
height = []
shape_setting = []
round_setting = [0]
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

    # 'n' is how many times we need to ask the user for the side / base / height of their shape
    n = formula_check(shape)
    loop_ran = 0

    # runs loop 'n' amount of times
    for item in range(n):
        length = number_checker(f"Length of Side {string_variables[0 + loop_ran]}: ", 'float',
                                'xxx')

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
    area = shape_formula(shape)[0]
    perimeter = shape_formula(shape)[1]

    # changes area to N/A if it's 0
    if area == 0:
        print("test if it's been through area")
        area = "N/A"
    else:
        area = f'{area:.{round_setting[0]}f}'

    # changes perimeter to N/A if it's 0
    if perimeter == 0:
        print("test if its been through perimeter")
        perimeter = "N/A"
    else:
        perimeter = f'{perimeter:.{round_setting[0]}f}'

    # results area
    results = f"Area: {area}\nPerimeter: {perimeter}"

    if shape == "circle":
        results = f"Area: {area}\nCircumference: {perimeter}"

    if shape == "triangle":
        # if 'b' is 0, only 1 variable was entered
        if b == 0:
            results = "Invalid Triangle: Only one value given."

        # Area can be N/A if triangle is impossible (or degenerate).
        elif area == "N/A":
            minimum = [i for i in variables if 0 < i < max(variables)]
            results = (f"Impossible Triangle: Value {max(variables)} is greater than"
                       f" the sum of the other 2 values {minimum[0], minimum[1]}.")

            # subtract every variable in the list by the next variable
            # and sum the result to check if it's 0
            if sum([variables[0 + i] - variables[1 + i] for i in sorted(variables, reverse=True)]) == 0:
                print("Sides: ", sum([variables[i] - variables[i + 1] for i in sorted(variables, reverse=True)]))
                results = (f"Degenerate Triangle: Sum of the shorter sides are equal to the longest side,"
                           " therefore the triangle has collapsed into a straight line with no area to calculate.")

    if shape == "trapezium":
        # checks if side 'c' was given for height calculation
        if c == 0 and height[0] == "no":
            results = "Invalid Trapezium: Side 'c' was not given for height calculation"
        elif a == b:
            results = "Invalid Trapezium: Bases 'a' and 'b' are equal to each-other."
            if a + b == c + d:
                results = "Invalid Trapezium: Bases 'a' and 'b' are equal to it's legs 'c' and 'd'."

    if variables[0] == 0:
        results = "No variable was entered."

    print(f"{results}")

    # Only do PANDAS if area is valid
    if area != "N/A":
        all_shapes.append(shape)
        all_area.append(area)
        all_perimeter.append(perimeter)

# Output area

# Checks if PANDAS has been done before output
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