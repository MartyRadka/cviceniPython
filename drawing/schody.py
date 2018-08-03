from turtle import forward, right, left, setup, goto, hideturtle, showturtle, penup, pendown, exitonclick

setup(width=1000, height=800)

hideturtle()        # Make the turtle invisible
penup()             # Pull the pen up – no drawing when moving
goto(-200, -200)    # move to new position
showturtle()        # Make the turtle visible
pendown()           # Pull the pen down – drawing when moving

for x in range(6):
    forward(50)
    left(90)
    forward(50)
    right(90)

exitonclick()
