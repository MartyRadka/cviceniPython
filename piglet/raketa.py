import pyglet
from math import sin
window = pyglet.window.Window(width=1000, height=700)

raketa_off = pyglet.image.load("obrazky/raketa_off.png")
raketa_on = pyglet.image.load("obrazky/raketa_on.png")


raketa = pyglet.sprite.Sprite(raketa_off)
raketa.x = window.width / 2 - 40


# pokud definujeme časový interval, fce musí pčijímat 1 parametr
def let(t):
    if raketa.y < window.height:
        raketa.y += 4
    else:
        raketa.y = - 60
    raketa.rotation = sin(raketa.y / 4)


def vykresli():
    window.clear()
    raketa.draw()


def horeni_zapni(t):
    raketa.image = raketa_on  # přenastavíme obrázek na on a voláme fci vypni
    pyglet.clock.schedule_once(horeni_vypni, 0.01)


def horeni_vypni(t):
    raketa.image = raketa_off  # přenastavíme obrázek na off a voláme fci zapni
    pyglet.clock.schedule_once(horeni_zapni, 0.01)


def odstartuj(t):
    # na základě tohohle intervalu poletí rychleji, nebo pomaleji
    pyglet.clock.schedule_interval(let, 1/60)


pyglet.clock.schedule_once(horeni_zapni, 1)
# do tohohle se můžou zakomponovat i eventy, kdy se odstartuje až po kliknutí...
pyglet.clock.schedule_once(odstartuj, 1.5)
window.push_handlers(on_draw=vykresli)

pyglet.app.run()
