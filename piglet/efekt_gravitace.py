import pyglet

window = pyglet.window.Window(width=1000, height=700)

ball = pyglet.image.load("obrazky/micek.png")


class Micek:
    def __init__(self, sprite, rychlost_x, rychlost_y, gravitace):
        self.sprite = sprite
        self.rychlost_x = rychlost_x
        self.rychlost_y = rychlost_y
        self.gravitace = gravitace


micek1 = Micek(sprite=pyglet.sprite.Sprite(img=ball),
               rychlost_x=6,
               rychlost_y=-6,
               gravitace=-2)

micek1.sprite.y = window.height - ball.height - 1  # -1 proto, aby míček neodletěl nahoru,
                                                   # protože první iterace proběhne ještě pře tim, než vidim pohyb
micek1.sprite.x = 1


def move(dt):
    micek1.rychlost_y += micek1.gravitace  # rychlost je záporná a zvýšená o gravitaci, míček bude přirozeně klesat

    if micek1.rychlost_y > 0:
        micek1.rychlost_y += micek1.gravitace

    if micek1.sprite.y >= window.height - ball.height or micek1.sprite.y <= 0:
        micek1.rychlost_y = - micek1.rychlost_y

    if micek1.sprite.x >= window.width - ball.width or micek1.sprite.x <= 0:
        micek1.rychlost_x = - micek1.rychlost_x

    micek1.sprite.x += micek1.rychlost_x
    micek1.sprite.y += micek1.rychlost_y


pyglet.clock.schedule_interval(move, 1 / 60)


def draw():
    window.clear()
    micek1.sprite.draw()


window.push_handlers(on_draw=draw)

pyglet.app.run()

