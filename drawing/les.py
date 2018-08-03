# Napis obrazek! Treba les ze stromu, mesto z domu, nebe z hvezd, dav ze smailiku, hradbu z vezi, zikkurat ze schodu
# Muzes pouzit i nejakou z funkci modulu random


from turtle import forward, left, right, setup, penup, pencolor, goto, pendown, exitonclick
from random import randrange

setup(width=1200, height=900)       # resize of turtle window


def branch_right(x):                # function of one right branch
    pencolor("Green")
    right(30)
    forward(50 + 5 * x)
    right(150)
    forward(35)


def trunk():                        # function of trunk
    pencolor("Brown")
    left(90)
    forward(30)
    right(90)
    forward(25.8)
    right(90)
    forward(30)
    left(90)
    pencolor("Green")
    forward(25)


def branch_left(y):                 # function of one left branch
    pencolor("Green")
    forward(35)
    right(150)
    forward(60 - 5 * y)
    left(150)


def movement_tree():                # function of the tree
    penup()
    a = randrange(-500, 500)        # random.randrange for axis x
    b = randrange(-300, 420)        # random.randrange for axis y
    goto(a, b)                      # go to new position x, y
    pendown()
    for x in range(3):
        branch_right(x)
        if x < 2:
            left(180)
        else:
            forward(25)
    trunk()
    for y in range(3):
        branch_left(y)
    right(180)


for i in range(20):
    movement_tree()


exitonclick()
