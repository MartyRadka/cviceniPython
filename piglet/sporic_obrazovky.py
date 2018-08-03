# efekt gravitace se provádí postupným zrychlováním a ten upravit, jestli objekt stoupá nebo klesá
# rozpohybuj míček jako míček, aby letěl jedním směrem, odrazí se a pak obrátí směr

import pyglet

window = pyglet.window.Window(width=1000, height=700)

ball = pyglet.image.load("obrazky/micek.png")


# sprite.scale = float(0.8) ---> kdybych ctěla změnit velikost míčku


class Micek:

    def __init__(self, sprite, rychlost_x, rychlost_y, gravitace):
        self.sprite = sprite
        self.rychlost_x = rychlost_x
        self.rychlost_y = rychlost_y
        self.gravitace = gravitace


micek1 = Micek(sprite=pyglet.sprite.Sprite(img=ball),
               rychlost_x=4,
               rychlost_y=8,
               gravitace=-2)


def move(dt):
    micek1.sprite.x += micek1.rychlost_x  # micek1.sprite.x x souradnice micku
    micek1.sprite.y += micek1.rychlost_y

    if micek1.sprite.y + micek1.rychlost_y <= 0 or micek1.sprite.y >= window.height - ball.height:
        micek1.rychlost_y = - micek1.rychlost_y

    if micek1.sprite.x >= window.width - ball.width or micek1.sprite.x <= 0:
        micek1.rychlost_x = - micek1.rychlost_x


pyglet.clock.schedule_interval(move, 1 / 60)


def draw():
    window.clear()
    micek1.sprite.draw()


window.push_handlers(on_draw=draw)

pyglet.app.run()


# zkontroluj spodní hranici a otoč směr a zrychli pohyb
# můžeme vytvořit víc míčků a můžeme je nechat pohybovat samotné, protože je máme v tom seznamu
# # druhý úkol, přidej další klíč rychlost, který se pohybuje od bodu 0 na ose y a zvyšuje se směrem nahoru a
# to samy udělej směrem dolů
# třetí úkol aby se odrážel různě i po ose x, nemusim nastavovat rotaci, protože když měnim směr,
# tak se odráží pod stejnym ůhlem
# další úkol - spoj s událostmi - po kliknutí někde na okno vytvoř míček
