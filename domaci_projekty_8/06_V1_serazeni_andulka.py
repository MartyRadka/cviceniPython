# Úkol 6 - Had byl pyšný na to, že je první v abecedě. Dokud nepřiletěla "andulka".
# Abys uklidnila hada, vytvoř funkci, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno
# (t.j.: vrátí ["had", "pes", "andulka", "kočka", "králík"])

# postup:   Máš seznam hodnot, které chceš seřadit podle nějakého klíče. Klíč se dá z každé hodnoty vypořítat
#           Vytvoř seznam dvojic (klíč, hodnota)
#           Seřaď tento seznam dvojic - dvojice se řadí nejdřív podle prvního prvku, pak druhého, atd...
#           Nakonec vytvoř ze seznamu dvojic opět jeden seznam hodnot

# Proč má zrovna had takové výsadní postavení, zjistíš později.


domaci_zvirata = ["pes", "kočka", "králík", "had"]
print(domaci_zvirata)

# připojení andulky
domaci_zvirata.append("andulka")
print(domaci_zvirata)
print()


# seznam klíčů, podle kterých se bude seznam abecedně řadit
seznam_klicu = [zvire[1:len(zvire)] for zvire in domaci_zvirata]
print(seznam_klicu)
print()


# seznam n-tic(klíč, hodnota)
seznam_dvojic = list(zip(seznam_klicu, domaci_zvirata))
print(seznam_dvojic)


# seřarení dvojic abecedně - ignoruje první písmeno
serazene_dvojice = sorted(seznam_dvojic)
print(serazene_dvojice)
print()


# konečný seznam hodnot
seznam_hodnot = [dvojice[1] for dvojice in serazene_dvojice]
print(seznam_hodnot)






