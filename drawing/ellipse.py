from turtle import shape, shapesize, tilt, fillcolor, pencolor, left, right, forward, stamp, penup, goto, circle, exitonclick

penup()             # no drawing
goto(2, 14)         # move to new position

shape("circle")     # drawing yellow shape circle
shapesize(7, 7)
fillcolor("yellow")
pencolor("darkRed")
stamp()

penup()             # no drawing
goto(0, -100)       # move to new position

shape("circle")     # drawing red ellipse
shapesize(5, 1, 2)
fillcolor("red")
pencolor("darkRed")

# for loop for ellipse
for x in range(72):
    forward(10)
    left(5)
    tilt(10)
    stamp()

exitonclick()

