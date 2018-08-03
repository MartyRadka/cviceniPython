# zadání úkolu 8 domácí projekty 5: Napiš program, který simuluje tuto hru:
# První hráč hází kostkou (vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka.
# Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází třetí a nakonec čtvrtý hráč.
# Vyhrává ten, kdo na hození šestky potřeboval nejvíce hodů. (Když shoda vyhraje ten, kdo házel dřív)
# Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál!

# tohle bude asi nej řešení...???

from random import randrange


def vypocitej_skore():
    skore = 0                               # skore = 0 je ve přímo funkci a vynuluje tak skore pro každého nového hráče
    while True:
        hod = randrange(1, 7)
        print("Hod je: {}".format(hod))
        if 1 <= hod <= 5:
            skore = skore + hod
            print("Skore je: {}".format(skore))
        elif hod == 6:
            return skore


max_skore = 0           # tohle max_skore = 0 je mimo for loop z důvodu, aby počáteční max_skore bylo nula
vitez = 0               # a to pouze jednou na začátku a ve for loopu je inicializované, aby si pamatovalo
                        # každé nové max_skore. Kdybych napsala přímo do for cyklu max_skore = 0
                        # tak potom by vždy pro každého hráče podmínka porovnávala aktuální skore s
                        # max_skore 0, takže by printla pokaždé, že prozatím vede tento hráč!!!!!


for hrac in range(1, 5):

    print("Hraje hráč číslo {}".format(hrac))
    aktualni_skore = vypocitej_skore()

    if aktualni_skore > max_skore:
        max_skore = aktualni_skore
        vitez = hrac
        print("Prozatím vede tento hráč se skóre: {}".format(max_skore))
    elif aktualni_skore == 0:
        print("Hráč prohrál, jeho skóre je {}".format(aktualni_skore))
    elif aktualni_skore < max_skore:
        print("Hráč prohrál, nedosahuje na nejvyšší skore")
    elif aktualni_skore == max_skore:
        print("Shoda, vyhrává hráč, který shodné skóre naházel dřív")
    print()

print("Vyhrává hráč {} s celkovým skóre {}".format(vitez, max_skore))

# if podmínka - pokud je aktuální_skore větší něž max_skore tedy inicializuje max_skore na aktualni_skore
# proto proměnná max_skore = aktualni_skore



