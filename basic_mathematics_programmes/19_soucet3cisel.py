# Napiš program, který se zeptá na 3 čísla a zjistí, jestli je jejich součet větší než 10.

cislo_1 = int(input("Zadej první číslo: "))
cislo_2 = int(input("Zadej druhé číslo: "))
cislo_3 = int(input("Zadej třetí číslo: "))

soucet = cislo_1 + cislo_2 + cislo_3

if soucet > 10:
    print("Součet čísel {}, {} a {} je roven {} a to je větší než 10!".format(cislo_1, cislo_2, cislo_3, soucet))
else:
    print("Součet čísel {}, {} a {} je roven pouze {}, není větší než 10".format(cislo_1, cislo_2, cislo_3, soucet))
