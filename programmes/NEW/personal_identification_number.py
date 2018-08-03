# Write functions. Each will have a string parameter of personal identification number (pin) and analyze it:

#   a) it's in correct format: 6 digits, slash, 4 digits (Return True or False)
#   b) it's divisible by 11 (Return True or False)
#   c) which date of birth is coded in first 6 digits? (Return tuple of int - day, month, year)
#   d) which sex appears in pin? (Return Man, or Woman)

# Write also the tests, if functions are correct
# Take personal identification numbers published only after 1985
# The real pins can be more difficult to treat

# String will be users input...

# -------------------------------------------------------------------------------------------------


import re


def get_users_input():
    return input("Enter your personal identification number (PIN): ").strip()


def is_pin_correct(string):
    """
    :return: True if correct format, else False
    """
    return re.match(r"^\d{6}/\d{4}$", string)  # same r"^[0-9]{6}/[0-9]{4}$"


def is_divisible_by_11(string):
    """
    :return: True if divisible by 11, else False
    """
    return int(string[:6] + string[7:11]) % 11 == 0


def get_day_of_birth(string):
    """
    :return: tuple of int
    """
    year = int(string[:2])
    month = int(string[2:4])
    day = int(string[4:6])
    if month > 62:
        raise ValueError("Year has only 12 months!")
    elif 12 < month <= 62:
        month -= 50
    if day > 31:
        raise ValueError("Month has 31 days (simplified)")
    return day, month, year


def get_gender(string):
    gender = ""
    if 12 < int(string[2:4]) <= 62:
        gender = "Woman"
    elif 0 < int(string[2:4]) <= 12:
        gender = "Man"
    return gender


if __name__ == "__main__":
    state = True
    while state:
        date_of_birth = get_users_input()
        if date_of_birth and is_pin_correct(date_of_birth) and is_divisible_by_11(date_of_birth):
            print(get_day_of_birth(date_of_birth))
            print(get_gender(date_of_birth))
            state = False
        else:
            print("Check your PIN! Use a good format YYMMDD/SSSC!")



