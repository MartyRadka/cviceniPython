from turtle import forward, left, right, speed, exitonclick


def get_integer():
    i = None
    while i is None:
        i = int(input("Chose a number of sides: "))
        if i <= 0:
            raise ValueError("Chose whole number greater than 0! ")
        return i


def draw_polygon(n):
    side = 500 / n
    interior_angle = 180 * (1 - 2 / n)
    angle = 180 - interior_angle

    for x in range(n):
        speed(3)
        forward(side)
        left(angle)


draw_polygon(get_integer())

exitonclick()

