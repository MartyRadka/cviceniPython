# Následující program vypíše čísla od - do, která zadáš.
# Místo čísel dělitelných 3 napíše \"bum\"
# místo čísel dělitelných 5 napíše \"bác\"
# a místo čísel dělitelných zároveň 3 i 5 napíše \"bum-bác\"

lower_base = int(input("Zadej spodní hranici: "))
upper_base = int(input("Zadej horní hranici: "))
print()

for cislo in range(lower_base, upper_base + 1):

    if cislo % 3 != 0 and cislo % 5 != 0:
        print(cislo)

    if cislo % 3 == 0 and cislo % 5 == 0:
        print("bum-bác")

    if cislo % 3 == 0 and cislo % 5 != 0:
            print("bum")

    if cislo % 5 == 0 and cislo % 3 != 0:
            print("bác")
