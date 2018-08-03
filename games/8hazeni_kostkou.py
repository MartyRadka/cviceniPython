# zadání úkolu 8 domácí projekty 5: Napiš program, který simuluje tuto hru:
# První hráč hází kostkou (vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka.
# Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází třetí a nakonec čtvrtý hráč.
# Vyhrává ten, kdo na hození šestky potřeboval nejvíce hodů. (Když shoda vyhraje ten, kdo házel dřív)
# Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál!


from random import randrange


def vypocitej_skore():
    skore = 0                               # skore = 0 je přímo ve funkci a vynuluje tak skore pro každého nového hráče
    while True:
        hod = randrange(1, 7)
        print("Hod je: ", hod)
        if 1 <= hod <= 5:
            skore = skore + hod
            print("Skore je: ", skore)
        elif hod == 6:
            return skore


max_skore = 0           # tohle max_skore = 0 je mimo for loop z důvodu, aby počáteční max_skore bylo nula
                        # a to pouze jednou na začátku a ve for loopu je inicializované, aby si pamatovalo
                        # každé nové max_skore. Kdybych napsala přímo do for cyklu max_skore = 0
                        # tak potom by vždy pro každého hráče podmínka porovnávala aktuální skore s
                        # max_skore 0, takže by printla pokaždé, že prozatím vede tento hráč!!!!!


for x in range(1, 5):

    aktualni_skore = vypocitej_skore()

    if aktualni_skore > max_skore:
        max_skore = aktualni_skore
        print("Prozatím vede tento hráč")
    elif aktualni_skore < max_skore:
        print("Hráč prohrál, nedosahuje na nejvyššní skore")
    else:
        print("Shoda")


# if podmínka pokud je aktuální_skore větší něž max_skore tedy inicializuje max_skore na aktualni_skore
# proto proměnná max_skore = aktualni_skore












"""hrac_1 = vypocitej_skore()
print("Hráč jedna získal:", hrac_1)
hrac_2 = vypocitej_skore()
print("Hráč dva získal:", hrac_2)
hrac_3 = vypocitej_skore()
print("Hráč tři získal:", hrac_3)
hrac_4 = vypocitej_skore()
print("Hráč čtyři získal:", hrac_4)"""


# print("Vyhrál hráč se skorem: ", max(hrac_1, hrac_2, hrac_3, hrac_4))           # takhle určitě neeee!


