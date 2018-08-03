from random import randrange


def vyhodnot(pole):
    # vyhodnotí stav hry
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def tah(pole, cislo_policka, symbol):
    # vzhled pole
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


def tah_hrace(pole):
    # Podmínky, za jakých může hráč hrát. Dostane řetězec s herním polem po tahu hráče
    while True:
        try:
            cislo_policka = int(input("Zadej číslo pole od 0 do 19: "))
        except ValueError:
            print("Zadej číslo! ")
        except Exception as e:
            print("Chyba:", e)
        else:
            print("Ok:", cislo_policka)
            return tah(pole, cislo_policka, "x")


def tah_pocitace(pole, symbol):
    # Dostane řetězec s herním polem po tahu počítače

    while True:
        if pole.find(symbol + symbol + "-") >= 0:
            cislo_policka = pole.find(symbol + symbol + "-") + 2
        elif pole.find("-" + symbol + symbol) >= 0:
            cislo_policka = pole.find("-" + symbol + symbol)
        elif pole.find(symbol + "-" + symbol) >= 0:
            cislo_policka = pole.find(symbol + "-" + symbol) + 1
        elif pole.find(symbol + "--") >= 0:
            cislo_policka = pole.find(symbol + "--") + 1
        elif pole.find("--" + symbol) >= 0:
            cislo_policka = pole.find("--" + symbol) + 1
        elif pole.find("-" + symbol + "-") >= 0:
            cislo_policka = pole.find("-" + symbol + "-")
        else:
            cislo_policka = randrange(len(pole))

        if pole[cislo_policka] == "-":
            print("Počítač hrál na pole číslo: {}".format(cislo_policka))
            return tah(pole, cislo_policka, symbol)
#0 <= cislo_policka <= 19 and


def piskvorky1d():
    hrac = "x"                            # jako první hraje hráč (vstupní nastavení proměnné hráč)
    pole = "-" * 20                       # velikost pole

    while True:                           # while cyklus
        if hrac == "x":                   # pokud hraje hráč
            pole = tah_hrace(pole)        # pole se změní na řetězec s tahem hráče
            hrac = "o"                    # jako další hraje počítač
        elif hrac == "o":                 # pokud hraje počítač
            pole = tah_pocitace(pole, "o")     # pole se změní na řetězec s tahem počítače
            hrac = "x"                    # jako další hraje hráč

        vysledne_pole = vyhodnot(pole)
        print(pole)
        print()

        if vysledne_pole != "-":          # if podmínka, která si volá returnované výsledky z fce vyhodnot(pole)
            if vysledne_pole == "x":
                print("Gratuluji! Vyhrál jsi.")
            elif vysledne_pole == "o":
                print("je mi líto, vyhrál počítač.")
            elif vysledne_pole == "!":
                print("Remiza")
            return


piskvorky1d()



