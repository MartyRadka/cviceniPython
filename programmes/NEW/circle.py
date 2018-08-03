# Get input from user - only float. And get circumference and aria of circle.

from math import pi
import re


def get_output():
    """
    :return: floating point number
    """
    output = input("Enter radius: ")
    if re.match(r"^\d+?\.\d+?$", output) is None or len(output) == 0:
        print("Wrong radius! Use float greater than zero!")
    else:
        return float(output)


def get_circumference(r):  # circumference or perimeter_of_circle
    return 2 * pi * r


def get_area_of_circle(r):
    return pi * r ** 2


state = True
while state:
    radius = get_output()
    if radius:
        print("Circumference: {}".format(get_circumference(radius)))
        print("Aria of circle: {}".format(get_area_of_circle(radius)))
        state = False


