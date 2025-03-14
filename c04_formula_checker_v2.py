import math


def formula_check(question, shapes_list, exit_code=None):
    """asks user for their chosen shape then
    calculates the chosen shape by their formula"""
    area = 0
    perimeter = 0

    error = "enter a valid shape"

    response = input(question).lower()

    if response == exit_code:
        return response

    try:
        if response in shapes_list:
            pass
        else:
            print("Invalid shape / Write the shape's full name.\n")

    except ValueError:
        print(error)

    # will replace values with random.randint()
    # and phrase question later on
    if response == "circle":
        radius = 0
        area = 2 * math.pi * radius

    # perhaps have 3 different types of triangles aka
    # right-angled, no 3rd side triangle (for perimeter question),
    # 3 side triangles

    elif response == "triangle":
        base = 0
        height = 0
        triangle_side = 0
        perimeter = base + height + triangle_side
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
        trapezium_base = 0
        base = 0
        height = 0
        perimeter = 0
        area = ((trapezium_base + base) / 2) * height

    return area, perimeter


# initialise variables

shapes = ["circle", "triangle", "rectangle", "square", "trapezium"]

while True:
    formula = formula_check("What shape are you solving? ", shapes)
    print(str(formula))
    print()
