from turtle import forward, right, left, setup, goto, hideturtle, showturtle, penup, pendown, exitonclick


setup(width=1200, height=900)      # setup the width and height fo window


hideturtle()        # hide pen
penup()             # Pull the pen up
goto(-200, -200)    # go to new position
showturtle()        # show pen
pendown()           # Pull the pen down


# example to see where is a new position
forward(100)
left(90)
forward(120)


exitonclick()
