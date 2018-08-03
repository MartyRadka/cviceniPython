# nakresli domecek: jak pravil Pythagoras, delka sikme cary v domecku je drha odmocnina krat delka steny.
# cara na strese je polovicni.

from turtle import forward, right, left, exitonclick

from math import sqrt

a = 50
b = sqrt(2) * a
c = b / 2

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
forward(a)

exitonclick()
