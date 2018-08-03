# Get input from user - both int or float. And get circumference and aria of circle.

from math import pi


def get_output():
    """
    :return: both int and float
    """
    return float(input("Enter radius: "))


def get_circumference(r):  # circumference or perimeter_of_circle
    return 2 * pi * r


def get_area_of_circle(r):
    return pi * r ** 2


if __name__ == '__main__':

    state = True
    while state:
        try:
            radius = get_output()
            if radius > 0:
                print("Circumference: {}".format(get_circumference(radius)))
                print("Aria of circle: {}".format(get_area_of_circle(radius)))
                state = False
            else:
                print("Must be greater than zero.")
        except ValueError:
            print("Wrong radius!")


