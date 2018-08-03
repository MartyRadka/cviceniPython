# nakresli 6 sestiuhelniku, ktere se navzajem dotykaji a vytvori tak 7 sestiuhelniku


from turtle import forward, left, right, exitonclick

n = 6
a = 200 / n
vnitrni_uhel = 180 * (1 - 2 / n)
uhel = 180 - vnitrni_uhel


for y in range(6):
    for x in range(6):
        forward(a)
        left(uhel)
    left(vnitrni_uhel)
    forward(a)
    right(uhel)


exitonclick()
