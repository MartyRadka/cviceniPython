import random


def hra(tah_cloveka):  # tah_cloveka = odpoved = kamen, nuzky, nebo papir
    mozne_tahy = ["kamen", "nuzky", "papir"]
    tah_pocitace = random.choice(mozne_tahy)

    print("Pocitac si vybral: {}".format(tah_pocitace))

    if tah_cloveka == tah_pocitace:
        return "remiza"
    elif tah_cloveka == "kamen" and tah_pocitace == "nuzky" or \
            tah_cloveka == "papir" and tah_pocitace == "kamen" or \
            tah_cloveka == "nuzky" and tah_pocitace == "papir":
        return "vyhral/a jsi!"
    elif tah_cloveka == "kamen" and tah_pocitace == "papir" or \
            tah_cloveka == "nuzky" and tah_pocitace == "kamen" or \
            tah_cloveka == "papir" and tah_pocitace == "nuzky":
        return "prohral/a jsi!"
    else:
        return "Nerozumím, zadej kamen, nuzky, papir, nebo konec! "


while True:
    odpoved = input("Chceš si zahrát? Zadej: \"kamen, nuzky, nebo papir\". Pokud ne, řekni \"konec\": ")
    if odpoved == "konec":
        print("Škoda! Hra ukončena uživatelem. ")
        break
    else:
        print(hra(odpoved))
