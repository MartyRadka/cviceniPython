import pyglet
window = pyglet.window.Window(width=1000, height=700)

obrazek = pyglet.image.load("obrazky/had.png")
# nactení obrázku

# třída Sprite (podle pep8 se píše s velkym písmenem) jejíž pomocí můžeme obrázek natácet, posouvat
had = pyglet.sprite.Sprite(obrazek)
had.x = window.width / 2 - had.width // 2
had.y = window.height / 2 - had.height // 2
# had má definovatelný atributy x a y a podle nich můžeme určit pozici hada, musíme to dělat responsivně
# když potřebujeme definovat víc prvků, tak si nadefinujeme seznam prvků a každý prvek bude mít vnitřní slovník
# [{"p": }, ] když upravuju, vyberu nějaký rpvek ze seznamu...
had.rotation = 30
# nastavení rotace doprava, pokud budu chtít dělat rotaci doleva, tak dám -30
# pyglet smaže prvky, když zajedu za okraj obrazovky, ale ošetřím to obnovováním!


def vykresli():
    window.clear()
    had.draw()


def klik(x, y, tlacitko, mod):
    print(tlacitko, mod)
    had.x = x
    had.y = y


window.push_handlers(on_draw=vykresli,
                     on_mouse_press=klik)

pyglet.app.run()
