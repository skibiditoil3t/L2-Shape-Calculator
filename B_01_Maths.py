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
    print("\n")
    print(make_statement("Instructions", "="))

    print("\nWelcome to the MHS Maths Shape Calculator!"
          "\n"
          "\nChoose from 5 shapes:"
          "\n'c' is circle | 's' is square | 'r' is rectangle | 't' is triangle or trapezium ."
          "\n[Alternate to 't' (and every other shape) is the first 3 letters]"
          "\n[E.G. 'Tri' --> Triangle, 'Tra' --> Trapezium]"
          "\n['t' can be overwritten by the first 3 letters of either triangle or trapezium]."
          "\n"
          "\nOnce you've chosen a shape, you'll be prompted to enter the length of the side /"
          "\nbase / height."
          "\n"
          "\nOnce you've completed all of the above, "
          "\nyou'll be able to view the shapes you've calculated on your computer."
          "\n"
          "\n"
          )
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

            elif response == i[:num_letters] or response == i[:3]:
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


def number_checker(question, exit_code=None):
    """Checks that the float value given is greater than zero"""

    error = "Enter a number greater than zero."

    while True:
        response = input(question).lower()

        if response == exit_code:
            return str(response)

        try:
            # change the response to a float and check that it's more than zero
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def formula_check(response, exit_code):
    """calculates the user's shape by the shape's according formula"""

    if response == exit_code:
        return response

    perimeter = 0
    area = 0

    # Response is matched with shape and calculated accordingly
    if response == "circle":
        perimeter = math.pi * (a * 2)
        area = math.pi * (a ** 2)

    elif response == "triangle":

        # checks if there's only 2 variables
        # programme assumes it's a right-angled triangle
        if b != 0:
            area = 1 / 2 * a * b
            perimeter = math.sqrt(a ** 2 + b ** 2)

            # checks if user has entered a 3rd variable
            # the triangle will be calculated using Heron's law
            if c != 0:
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

        # If only one side is given, we only print out the error.
        else:
            print("Invalid Triangle: Only one value given.")

    elif response == "rectangle":
        area = ((a ** 2) * (b ** 2))
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
    if shape in shape_list:

        if shape == "triangle" and b != 0 and c == 0:
            string = ("\nArea:", area,
                  "Hypotenuse:", perimeter)

        # If the 4th side isn't given in a trapezium,
        # the programme assumes the user only wants to solve for area.
        elif shape == "trapezium" and (a and b and c) > 0 and d == 0:
            perimeter = "N/A"
            string = ("\nArea:", area,
                  "Perimeter:", perimeter)

        elif shape == "circle":
            string = ("\nArea:", area,
                  "Circumference:", perimeter)
        elif perimeter <= 0 and area <= 0:
            string = (f"The area / perimeter must be non-negative or not equal to 0, "
          f"please check your values.")


    string = ("\nArea:", area,
              "Perimeter:", perimeter)

    if perimeter <= 0 or area <= 0:

        area = "N/A"
        perimeter = "N/A"

    print(string)

    all_shapes.append(response)
    all_area.append(area)
    all_perimeter.append(perimeter)

    return area, perimeter


# initialise variables
loop_ran = 0

# lists
shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]
shape_setting = []
all_shapes = []
all_area = []
all_perimeter = []

# PANDAS dictionary
shape_calc_dict = {
    "Shape": all_shapes,
    "Area": all_area,
    "Perimeter": all_perimeter,
}

# Ask user if they want instructions
want_instructions = yes_no("Do you want instructions? ")

if want_instructions == "yes":
    instruction()

# math loop starts
while True:

    # empty list to put variables in, prevents 'too many unpacked' error
    variables = []

    # ask user for the shape
    shape = string_checker("\nWhat shape are you solving? ", 1, shape_list)

    # 'n' is how many times we need to ask the user for the side / base / height of their shape
    # shape_setting.insert works as an optimized way to overwrite 't'
    if shape == "xxx":
        break
    elif shape == "square" or shape == "circle":
        n = 1
    elif shape == "rectangle":
        n = 2
    elif shape == "triangle":
        sides = yes_no("Do you have 3 sides?")

        if sides == "yes":
            n = 3

        n = 2
        shape_setting.insert(0, shape)
    else:
        n = 4
        shape_setting.insert(0, shape)

    # runs loop 'n' amount of times
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

# Output area

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