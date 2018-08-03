# Nakresli kytku podle predlohy

from turtle import forward, left, right, setup, goto, hideturtle, showturtle, penup, pendown, exitonclick
from math import pi

setup(width=1200, height=900)      # resize of turtle window

# setup for new position of the pen

hideturtle()        # hide pen
penup()             # Pull the pen up
goto(0, 200)        # go to new position
showturtle()        # show pen
pendown()           # Pull the pen down


def draw_arc_right(r):      # function for right arc
    c = 2 * pi * r          # Circumference of circle
    ca = c / (360 / 60)     # Circumference of arc (assume 60 degree central angle of sector as above)
    n = int(ca / 3) + 1     # number of segments
    l = ca / n              # length of segment
    for i in range(n):
        forward(l)
        left(360 / (n * 6))


def draw_arc_left(r):       # function for left arc
    c = 2 * pi * r          # Circumference of circle
    ca = c / (360 / 60)     # Circumference of arc (assume 60 degree central angle of sector as above)
    n = int(ca / 3) + 1     # number of segments
    l = ca / n              # length of segment
    for i in range(n):
        forward(l)
        right(360 / (n * 6))


def draw_xleaf(r):          # function for whole leaf on the right and the part of stem
    draw_arc_right(r)
    left(180 - 60)
    draw_arc_right(r)
    left(30)


def draw_yleaf(r):          # function for whole leaf on the left and the part of stem
    draw_arc_left(r)
    right(180 - 60)
    draw_arc_left(r)
    right(30)


# for loop for draw petals
for y in range(18):
    left(20)
    for x in range(4):
        forward(50)
        left(90)
right(90)
penup()
forward(50)
pendown()
forward(50)
left(90)

# for loop for the leaves and stem
for z in range(0, 120, 20):
    draw_xleaf(60 + z)
    forward(20 + z / 4)
    right(90)
    draw_yleaf(65 + z)
    forward(20 + z / 4)
    left(90)

exitonclick()


