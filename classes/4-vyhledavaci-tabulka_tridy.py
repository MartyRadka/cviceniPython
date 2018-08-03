# Dictionary - list of same values where we search with keys

# Use class instead of dictionary


class Person:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return "Name: {} \nPhone number: {} \nAddress: {}".format(self.name, self.phone_number, self.address)

    def get_phone_number(self):
        print("{} has a phone number: {}".format(self.name, self.phone_number))

    def get_address(self):
        print("{} live at: {}".format(self.name, self.address))


person1 = Person("Jan Novák", "000000000", "Ke Karlovu 2, Praha")
person2 = Person("Markéta Novotná", "111111111", "Znojemská 6, Praha")
person3 = Person("Petr Kovář", "222222222", "Teplická 9, Praha")
person4 = Person("Zuzana Marková", "333333333", "Mariánské náměstí 13/1, Praha")
person5 = Person("Jana Novotná", "444444444", "Smržová 165/8, Praha")
person6 = Person("Daniel Vrána", "555555555", "Růžová 3, Praha")
person7 = Person("Jiří Rokos", "666666666", "Ke Kačírku 5, Praha")
person8 = Person("Miroslava Tichá", "777777777", "Skála 14/2, Praha")

people = [person1, person2, person3, person4, person5, person6, person7, person8]

person3.get_phone_number()
person8.get_address()
print()

for person in people:
    person.get_phone_number()
print()

for person in people:
    person.get_address()

