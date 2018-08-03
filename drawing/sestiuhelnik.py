from turtle import forward, left, right, speed, exitonclick

n = 6
a = 200 / n
vnitrni_uhel = 180 * (1 - 2 / n)
uhel = 180 - vnitrni_uhel

# tohle nakresli peknou origamy kytku
for y in range(6):
    speed(3)
    left(uhel)
    for x in range(6):
        forward(a)
        left(uhel)

exitonclick()
