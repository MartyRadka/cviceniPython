# Úkol 0 - Napiš fci, která pro argumentem zadané číslo n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné
# do n a jako hodnoty k nim jejich druhé mocniny

# Úkol 1 - Napiš fci, která sečte a vrátí sumu všech klíčů a sumu všech hodnot ve slovníku, který dostane jako argument
# K vyzkoušení můžeš použít slovník z minulé úlohy

# Úkol 2 - Napiš fci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé znaky
# ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci

# úkol 3 - Napiš fci, která vypíše obsah slovníku (klíče a k nim náležící hodnoty) na jednotlivé řádky.
# Fci, která něco vypisuje, je vhodné pojmenovat speciálně, zde třeba vypis_slovnik(), aby bylo jasné, že jen
# vypisuje a nic nevrací.


def get_dictionary_number_power(n):
    number_power_dict = {}
    for i in range(1, n + 1):
        number_power_dict[i] = i ** 2
    return number_power_dict


def count_sum_keys_values(dictionary):
    keys_values_sum = dict(dictionary)  # pro zachování původního vytvořen nový dict
    return sum(keys_values_sum.keys()), sum(keys_values_sum.values())


def make_dict_from_str(string):
    dictionary = {}
    for char in string:
        dictionary[char] = dictionary.get(char, 0) + 1
        # d.get(k, h) = výběr, h pokud záznam neexistuje - pokud nebude + 1 value == 0
    return dictionary


def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print("{}: {}".format(key, value))


def get_input():
    i = int(input("Write whole number (integer): "))
    if i < 0:
        raise Exception("Number has not to be negative!")
    return i


def check_input():
    while True:
        try:
            i = get_input()
        except Exception as e:
            print("chyba: ", e)
        else:
            print("OK:", i)
            return i


print(get_dictionary_number_power(check_input()))
print(count_sum_keys_values(get_dictionary_number_power(check_input())))
print(make_dict_from_str("Moje dcera má ráda čokoládu!"))
letter_occurrence = {'M': 1, 'o': 3, 'j': 1, 'e': 2, ' ': 4, 'd': 3, 'c': 1, 'r': 2, 'a': 2, 'm': 1, 'á': 3}
print_dictionary(letter_occurrence)
