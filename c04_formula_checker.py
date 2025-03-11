import math


def shape_check(question, shapes):
    """asks user for their chosen shape"""
    error = "enter a valid shape"

    while True:
        response = input(question).lower()

        try:
            if response in shapes:
                return response
            else:
                print("that isn't a valid shape, try again\n")
        except ValueError:
            print(error)


def formula_check(response):
    """calculates the chosen shape by their formula"""
    area = 0

    if response == "circle":
        radius = 0
        area = 2 * math.pi * radius
    elif response == "triangle":
        base = 0
        height = 0
        area = 1 / 2 * base * height
    elif response == "rectangle":
        length = 0
        width = 0
        area = length * width
    elif response == "square":
        a = 0
        area = a ^ 2
    elif response == "trapezium":
        a = 0
        base = 0
        height = 0
        area = ((a + base) / 2) * height
    return area


# initialise variables
pi = math.pi

shapes_list = ["circle", "triangle", "rectangle", "square", "trapezium"]

while True:
    shape = shape_check("what shape do u want ", shapes_list)
    formula = formula_check(shape)
    print(shape, formula)
    print()
