# Draw a village


from turtle import forward, right, left, setup, goto, hideturtle, showturtle, penup, pendown, exitonclick
from math import sqrt

setup(width=1200, height=900)


a = 50
b = sqrt(2) * a
c = b / 2

hideturtle()        # make turtle invisible
penup()             # Pull the pen up - no drawing
goto(-200, -200)    # go to new position
showturtle()        # make turtle visible
pendown()           # pull the pen down - drawing

for z in range(10):
    left(90)
    for x in range(3):
        forward(a)
        right(90)
    right(45)
    forward(b)
    for y in range(2):
        right(90)
        forward(c)
    right(90)
    forward(b)
    left(90 + 45)
    forward(a + 20)

exitonclick()
