from turtle import forward, left, right, speed, exitonclick

n = 8
a = 200 / n
vnitrni_uhel = 180 * (1 - 2 / n)
uhel = 180 - vnitrni_uhel

for x in range(8):
    speed(3)
    forward(a)
    left(uhel)

exitonclick()