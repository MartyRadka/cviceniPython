# nakresli spiralu
# tip: n-ty uhelnik, zvetsujici se pri kazde otocce o x

from turtle import forward, left, right, exitonclick

n = 100
a = 0.5 / n
vnitrni_uhel = 180 * (1 - 2 / n)
uhel = 180 - vnitrni_uhel

for x in range(1000):
    forward(a * x)
    left(uhel)

exitonclick()

