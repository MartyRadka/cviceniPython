# Napiš program, který načte číslo a zjistí, jestli je sude (tj: dělitelné dvěmi beze zbytku)
# Pro připomenutí: Množinu všech sudých čísel lze zapsat jako: Sudá = 2Z = { …, −4, −2, 0, 2, 4, … }

cislo = int(input("Zadej libovolné celé číslo: "))

if cislo % 2 == 0:
    print("Číslo {} je sudé číslo.".format(cislo))
else:
    print("Číslo {} není dělitelné 2 beze zbytku - je tedy liché číslo".format(cislo))

