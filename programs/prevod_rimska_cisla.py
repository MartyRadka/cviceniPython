# Napiš fci, která převede římské číslice na číslo (int)


def preved_do_arabstiny(retezec):
    rimska_cisla = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    arabske_cislo = 0
    for index in range(len(retezec)):
        if index > 0 and rimska_cisla[retezec[index]] > rimska_cisla[retezec[index - 1]]:
            arabske_cislo += rimska_cisla[retezec[index]] - 2 * rimska_cisla[retezec[index - 1]]
        else:
            arabske_cislo += rimska_cisla[retezec[index]]
    return arabske_cislo


while True:
    try:
        rimske_cislo = input("Zadej libovolé římské číslo max do 3999: ").upper().strip()
        neplatne_cislo = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
        if rimske_cislo in neplatne_cislo:
            raise ValueError("Neplatné římské číslo: {}".format(neplatne_cislo))
        if rimske_cislo == "":
            raise AttributeError("Zadej, prosím, znovu! ")
    except Exception as e:
        print("Chyba: ", e)
    else:
        print(preved_do_arabstiny(rimske_cislo))



