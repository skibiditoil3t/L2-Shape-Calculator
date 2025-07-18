import math


variables = [2, 2, 2, 2]
a, b, c, d = variables


shape_list = ["circle", "triangle", "rectangle", "square", "trapezium"]
round_setting = 0

print(variables)


def formula_check(response, exit_code):
    """calculates the user's shape by the shape's according formula
        and outputs the results"""

    # initialise variables
    area = 0
    perimeter = 0
    results = "Area: whatever\nPerimeter: 0"

    for k in response:

          if k == exit_code:
              return response

          # match response with shape and calculate area (perimeter too if possible)
          if k == "circle":
              print(variables)
              perimeter = math.pi * (a * 2)
              area = math.pi * (a ** 2)
              results = f"Area: {area}\nPerimeter: {perimeter}"

          elif k == "triangle":

              # if 2nd side isn't 0, calculate a right-angled triangles area
              if b != 0:
                  area = 1 / 2 * a * b
                  perimeter = "N/A"

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
                          area = "N/A"
                          perimeter = "N/A"

              # If only one side is given, we only print out the error.
              else:
                  results = "Invalid Triangle: Only one value given."

          elif k == "rectangle":
              area = a * b
              perimeter = (a * 2) + (b * 2)

          elif k == "square":
              area = a ** 2
              perimeter = a * 4

          # need to check which is height and the parallel sides
          elif k == "trapezium":
              area = ((a + b) / 2) * c
              perimeter = "N/A"
              if d > 0:
                  perimeter = a + b + c + d

          round(area, 0)

          # # PANDAS area
          # all_shapes.append(response)
          # all_area.append(area)
          # all_perimeter.append(perimeter)

    return results

for item in shape_list:
      formula = formula_check(item, "xxx")
      print(f"Results for {item}:\n"
            f"{formula}\n")

