# Pomocí cyklu for a příkazu if napiš program, který z jednotlivých 'X' a mezer vypíše:
# X X X X X X
# X         X
# X         X
# X         X
# X         X
# X X X X X X

# uživatel zadává velikost čtverce
velikost_ctverce = int(input("Zadej velikost čtverce: "))
print()

for osa_y in range(velikost_ctverce):
    for osa_x in range(velikost_ctverce):
        if 0 < osa_x < velikost_ctverce - 1 and 0 < osa_y < velikost_ctverce - 1:
            print(" ", end=" ")
        else:
            print("X", end=" ")
    print()


