def zjisti_inicialy(zadani_jmeno, zadani_prijmeni):

    while zadani_jmeno == "":
        zadani_jmeno = input("Zadej tvé křestní jméno: ").strip().upper()

    while zadani_prijmeni == "":
        zadani_prijmeni = input("Zadej tvé příjmení: ").strip().upper()

    inicialy = zadani_jmeno[0] + zadani_prijmeni[0]
    print(zadani_jmeno + " " + zadani_prijmeni)
    return "Tvé iniciály jsou: {}".format(inicialy)


jmeno = input("Zadej tvé křestní jméno: ").strip().upper()
prijmeni = ""

print(zjisti_inicialy(jmeno, prijmeni))


