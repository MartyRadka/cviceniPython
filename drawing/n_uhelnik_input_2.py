from turtle import forward, left, right, speed, exitonclick


def get_integer():
    output = input("Chose a number of sides: ")
    if not output.isdigit() or int(output) <= 0:
        print("Wrong input! ")
    else:
        return int(output)


def draw_polygon(n):
    side = 500 / n
    interior_angle = 180 * (1 - 2 / n)
    angle = 180 - interior_angle

    for x in range(n):
        speed(3)
        forward(side)
        left(angle)


state = True
while state:
    number = get_integer()
    if number:
        draw_polygon(number)
        state = False


exitonclick()

