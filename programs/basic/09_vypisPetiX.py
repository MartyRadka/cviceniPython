# Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# X X X X X

# Osa x obsahuje 5 krát X. Na konci každého X je místo nového řádku mezera + print na další řádek
# for osa_x in range(5):
#     print("X", end=" ")
# print()

# Osa y obsahuje pětkrát for loop s osou x
pocet_radku = int(input("Kolik řádků s \"X\" chceš vypsat? "))
pocet_sloupcu = int(input("A kolik sloupců s \"X\" chceš vypsat? "))
print()

for osa_y in range(pocet_radku):
    for osa_x in range(pocet_sloupcu):
        print("X", end=" ")
    print()



