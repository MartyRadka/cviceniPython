from random import randrange, choice
from collections import namedtuple

VELIKOST_POLE = 20

SYMBOL_REMIZA = "!"

SYMBOL_PRAZDNE_POLICKO = "-"

VYHERNI_LIMIT = 6

SYMBOL_POCITAC = "o"

SYMBOL_HRAC = "x"  # konstanta


def vyhodnot(pole):
    # vyhodnotí stav hry
    if VYHERNI_LIMIT * SYMBOL_HRAC in pole:
        return SYMBOL_HRAC
    elif VYHERNI_LIMIT * SYMBOL_POCITAC in pole:
        return SYMBOL_POCITAC
    elif SYMBOL_PRAZDNE_POLICKO not in pole:
        return SYMBOL_REMIZA
    else:
        return SYMBOL_PRAZDNE_POLICKO


def tah(pole, cislo_policka, symbol):
    # vzhled pole
    pole = pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    return pole


def tah_hrace(pole):
    # Podmínky, za jakých může hráč hrát. Dostane řetězec s herním polem po tahu hráče
    while True:
        cislo_policka = int(input("Zadej číslo pole od 0 do 19: "))
        if 0 <= cislo_policka <= 19 and pole[cislo_policka] != SYMBOL_PRAZDNE_POLICKO:
            print("Pozice obsazena")
        elif 0 <= cislo_policka <= 19:
            return tah(pole, cislo_policka, SYMBOL_HRAC)
        else:
            print("Špatně, musíš zadat číslo od 0 do 19! ")


StavHry = namedtuple("StavHry", ["pole", "posledni_tah"])


def tah_pocitace(pole):
    # Dostane řetězec s herním polem po tahu počítače

    vychozi_policko = None
    try:
        policko_se_symbolem_pocitace = pole.index(SYMBOL_POCITAC)
        vychozi_policko = policko_se_symbolem_pocitace
    except ValueError:
        delka_pole = len(pole)
        nahodne_policko = randrange(delka_pole)
        vychozi_policko = nahodne_policko

    prazdne_policko = najdi_prazdne_policko_do_limitu(pole, vychozi_policko)

    if prazdne_policko is None:
        prazdne_policko = najdi_prazdne_policko_nahodne(pole)

        if prazdne_policko is None:
            raise Exception("REMIZA")

    print("Počítač hrál na pole číslo: {}".format(prazdne_policko))
    return tah(pole, prazdne_policko, SYMBOL_POCITAC)


def najdi_prazdne_policko_nahodne(pole):
    # prazdna_policka = []
    # for cislo_policka, policko in pole.items():
    #     if policko == SYMBOL_PRAZDNE_POLICKO:
    #         prazdna_policka.append(cislo_policka)

    prazdna_policka = (cislo_policka for cislo_policka, policko in pole.items() if
                       policko == SYMBOL_PRAZDNE_POLICKO)

    nahodne_prazdne_policko = choice(prazdna_policka)
    return nahodne_prazdne_policko


def najdi_prazdne_policko_do_limitu(pole, vychozi_policko):
    policko_vlevo = policko_vpravo = vychozi_policko
    for x in range(VYHERNI_LIMIT):
        policko_vlevo = zjisti_policko_vlevo(policko_vlevo)
        policko_vpravo = zjisti_policko_vpravo(policko_vpravo)

        if pole[policko_vlevo] == SYMBOL_PRAZDNE_POLICKO:
            return policko_vlevo
        elif pole[policko_vpravo] == SYMBOL_PRAZDNE_POLICKO:
            return policko_vpravo


def zjisti_policko_vpravo(soucasny_tah):
    policko_vpravo = min(soucasny_tah + 1, VELIKOST_POLE)
    return policko_vpravo


def zjisti_policko_vlevo(soucasny_tah):
    policko_vlevo = max(soucasny_tah - 1, 0)
    return policko_vlevo


def piskvorky1d():
    hrac = SYMBOL_HRAC  # jako první hraje hráč (vstupní nastavení proměnnéhráč)
    pole = SYMBOL_PRAZDNE_POLICKO * VELIKOST_POLE  # velikost pole

    while True:                             # while cyklus
        if hrac == SYMBOL_HRAC:             # pokud hraje hráč
            pole = tah_hrace(pole)          # pole se změní na řetězec s tahem hráče
            hrac = SYMBOL_POCITAC           # jako další hraje počítač
        elif hrac == SYMBOL_POCITAC:        # pokud hraje počítač
            pole = tah_pocitace(pole)       # pole se změní na řetězec s tahem počítače
            hrac = SYMBOL_HRAC              # jako další hraje hráč

        vysledne_pole = vyhodnot(pole)
        print(pole)
        print()

        if vysledne_pole != SYMBOL_PRAZDNE_POLICKO:          # if podmínka, která si volá returnované výsledky z fce vyhodnot(pole)
            if vysledne_pole == SYMBOL_HRAC:
                print("Gratuluji! Vyhrál jsi.")
            elif vysledne_pole == SYMBOL_POCITAC:
                print("je mi líto, vyhrál počítač.")
            elif vysledne_pole == SYMBOL_REMIZA:
                print("Remiza")
            return


piskvorky1d()



