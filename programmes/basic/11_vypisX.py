# Napiš program, který postupně z jednotlivých 'X' vypíše:
# X
# X X
# X X X
# X X X X

velikost_trojuhelniku = int(input("Zadej počet řádků: "))

for cislo_y in range(velikost_trojuhelniku):
    for cislo_x in range(cislo_y + 1):
        print("X", end=" ")
    print()
