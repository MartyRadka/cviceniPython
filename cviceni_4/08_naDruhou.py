# Pomocí cyklu for napiš program, který vypíše toto:
# 0 na druhou je 0
# 1 na druhou je 1
# 2 na druhou je 4
# 3 na druhou je 9
# 4 na druhou je 16

pocet_cisel = int(input("Kolik čísel chceš umocnit na druhou? "))

for cislo in range(pocet_cisel):
    print("{} na druhou je {}".format(cislo, cislo ** 2))
