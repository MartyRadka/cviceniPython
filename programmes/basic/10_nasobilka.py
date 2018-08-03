# Napiš program, který vypíše tabulku s násobilkou:
# 0 0 0 0 0
# 0 1 2 3 4
# 0 2 4 6 8
# 0 3 6 9 12
# 0 4 8 12 16

print("Následující program vytvoří tabulku s násobilkou na základě počtu čísel, které si vybereš...")
pocet_cisel = int(input("Zadej počet čísel: "))

for cislo_y in range(pocet_cisel):
    for cislo_x in range(pocet_cisel):
        print(cislo_x * cislo_y, end=" ")
    print()
