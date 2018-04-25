# Úkol 6 - Had byl pyšný na to, že je první v abecedě. Dokud nepřiletěla "andulka".
# Abys uklidnila hada, vytvoř funkci, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno
# (t.j.: vrátí ["had", "pes", "andulka", "kočka", "králík"])

# postup:   Máš seznam hodnot, které chceš seřadit podle nějakého klíče. Klíč se dá z každé hodnoty vypořítat
#           Vytvoř seznam dvojic (klíč, hodnota)
#           Seřaď tento seznam dvojic - dvojice se řadí nejdřív podle prvního prvku, pak druhého, atd...
#           Nakonec vytvoř ze seznamu dvojic opět jeden seznam hodnot

# Proč má zrovna had takové výsadní postavení, zjistíš později.

from operator import itemgetter


domaci_zvirata = ["pes", "kočka", "králík", "had"]
print(domaci_zvirata)

domaci_zvirata.append("andulka")
print(domaci_zvirata)
print()

# seřadí seznam podle klíče = druhého písmene
serazena_domaci_zvirata = sorted(domaci_zvirata, key=itemgetter(1))
print(serazena_domaci_zvirata)





