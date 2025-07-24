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
            settings["round"] = number_checker("Round to: ")
            return "round"

        # iterates through every item in a list and checks
        # if it matches the user's response
        for i in valid_ans_list:
            if response == i or response == i[:num_letters] or response == i[:3]:
                return i

            elif response == "t":

                # Returns the shape set to 't' if it's already there
                if ("triangle" or "trapezium") in settings:
                    return settings["t"]

                option = yes_no("\nDefault shape for 't' is triangle. Change to trapezium? ")

                settings["t"] = "triangle"

                if option == "yes":
                    settings["t"] = "trapezium"

                return settings["t"]

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
        sides = yes_no("Do you have 3 sides? ")

        i = 2
        text_formula = "a * b / 2"

        if sides == "yes":
            i = 3
            text_formula = "\U0000221As(s-a)(s-b)(s-c)"
            additional_info = "['s' is calculated after a, b and c are given].\n"

        settings["sides"] = i

    else:
        i = 4
        text_formula = "(a + b / 2) * Height"
        additional_info = "a = shorter base, b = longer base, c and d = legs\n"

        h = number_checker("Length of Height ('xxx' if you don't have): ", "float",
                           "xxx")

        settings["height"] = h

        if h == "xxx":
            additional_info = ("a = shorter base, b = longer base, c and d = legs\n"
                               "\nAll variables are required to calculate the height.\n")

    # print the shape's area formula and additional info if needed
    print("")
    print(make_statement(f"Area Formula: {text_formula} ", "="))
    print(additional_info, "")

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
        s = (a + b + c) / 2

        if settings["sides"] == 3:
            try:
                shape_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                shape_perimeter = a + b + c

            except ValueError:
                shape_area = 0

    elif response == "rectangle":
        shape_area = a * b
        shape_perimeter = (a * 2) + (b * 2)

    elif response == "square":
        shape_area = a ** 2
        shape_perimeter = a * 4

    elif response == "trapezium":
        if settings["height"] == "xxx":
            try:
                x = ((b - a) + (c**2 - d**2)/(b - a))/2
                if d != 0:
                    h = round(math.sqrt(c ** 2 - x ** 2), settings["round"])
            except ZeroDivisionError:
                pass
        else:
            h = settings["height"]

        shape_area = (a + b) * h / 2

        # If the bases are equal to each-other / longer base is less than shorter base,
        # area can't be calculated.
        if a == b or b < a:
            shape_area = 0
        elif d > 0:
            shape_perimeter = a + b + c + d

    return shape_area, shape_perimeter


# lists
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]
string_variables = ['a', 'b', 'c', 'd']
all_shapes = []
all_area = []
all_perimeter = []

# settings and PANDAS dictionary
settings = {
    "t": "",
    "round": 0,
    "height": 0,
    "sides": 0,
}

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

    # 'n' is how many sides need to be entered
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

    # round area / perimeter if it isn't 0
    if area == 0:
        area = "N/A"
    else:
        area = f'{area:.{settings["round"]}f}'

    if perimeter == 0:
        perimeter = "N/A"
    else:
        perimeter = f'{perimeter:.{settings["round"]}f}'

    # results area
    results = f"Area: {area}\nPerimeter: {perimeter}"

    if shape == "circle":
        results = f"Area: {area}\nCircumference: {perimeter}"

    if shape == "triangle":
        # if 'b' is 0, only 1 variable was entered
        if b == 0:
            results = "Invalid Triangle: Only one value given."

        # area can be N/A if triangle is impossible (or degenerate)
        elif area == "N/A":
            if loop_ran == 3:
                minimum = [i for i in variables if 0 < i < max(variables)]
                results = (f"Impossible Triangle: One variable ({max(variables)}) is greater than"
                           f"\nthe sum of the other two variables {minimum[0], minimum[1]}.")
            else:
                results = f"Invalid Triangle: Only 2 variables entered for a 3-sided triangle."

            # sort variables from biggest to smallest then sum to 0
            # to check for degenerate triangle
            variables = sorted(variables[:-1], reverse=True)
            if (variables[0] - variables[1] - variables[2]) == 0:
                results = ("Degenerate Triangle: Triangle is 'collapsed' due to variables"
                           "\nnot meeting the triangle inequality theorem.")

    if shape == "trapezium":

        if a == b:
            results = "Invalid Trapezium: Both bases can't be the same in a trapezium."
            if a + b == c + d:
                results = "Invalid Trapezium: Both bases can't be the same as both legs."

        # checks if side 'd' was entered as it's needed to calculate height
        elif settings["height"] == "xxx" and d == 0:
            results = f"Invalid Trapezium: Only {n}/4 variables were entered to calculate height."

        # if no other condition matches the error, output this one to user instead
        elif area == "N/A":
            results = "Invalid Trapezium: Please re-check your variable values."

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