# Úkol 6 - Had byl pyšný na to, že je první v abecedě. Dokud nepřiletěla "andulka".
# Abys uklidnila hada, vytvoř funkci, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno
# (t.j.: vrátí ["had", "pes", "andulka", "kočka", "králík"])

# postup:   Máš seznam hodnot, které chceš seřadit podle nějakého klíče. Klíč se dá z každé hodnoty vypořítat
#           Vytvoř seznam dvojic (klíč, hodnota)
#           Seřaď tento seznam dvojic - dvojice se řadí nejdřív podle prvního prvku, pak druhého, atd...
#           Nakonec vytvoř ze seznamu dvojic opět jeden seznam hodnot

# Proč má zrovna had takové výsadní postavení, zjistíš později.


animals = ["pes", "kočka", "králík", "had"]
print(animals)

animals.append("andulka")
print(animals)
print()


def order_list(list):
    """

    :param list: list of animals
    :return: ordered list of animals by alphabet without counting the first letter
    """
    list_pairs = [(animal[1:], animal) for animal in list]
    ordered_pairs = sorted(list_pairs)
    list_values = [pair[1] for pair in ordered_pairs]
    return list_values


print(order_list(animals))








