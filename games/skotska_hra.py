# Úkolem je vytvořit známou skotskou hru "Kdo? S kým? Co dělali?". Hra se hráče zeptá postupně na různé otázky,
# např.: "Kdo?", "S kým", "Co dělali?", "Kde?", "Kdy?", a nakonec "Proč?", s tím, že mu umožní na jednu otázku
# odpovědět vícekrát a všechny odpovědi si uloží.
# Na závěr pak hra z každé sady odpovědí vybere náhodně jednu odpověď a z takto vybraných odpovědí složí větu,
# kterou vypíše uživateli.
# Seznam otázek by mělo být mělo být možné změnit na jednom místě bez zásahu do logiky programu.

import random

print("Na níže položené otázky, můžež odpovědět kolikrát chceš, ale každou odpověď odděl čárkou!\n"
      "Pokud neoddělíš, tak budou všechny odpovědi brány jako jedna jediná odpověď :)")

otazky = {
    "Kdo? ": [],
    "S kým? ": [],
    "Co dělali? ": [],
    "Kde? ": [],
    "Proč? ": []
}

veta = []

for k in otazky:
    while len(otazky[k]) == 0:
        otazky[k] = input(k).strip()
    slovo = random.choice(otazky[k].split(",")).strip()
    veta.append(slovo)

print(" ".join(veta).capitalize())

