# Pomocí cyklu for napiš program, který vypíše toto:
# Řádek 0
# Řádek 1
# Řádek 2
# Řádek 3
# Řádek 4

pocet_radku = int(input("Kolik řádků chceš vypsat? "))

for cislo_radku in range(pocet_radku):
    print("Řádek {}".format(cislo_radku))
