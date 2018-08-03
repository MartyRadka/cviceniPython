import random
# 0 equal Tie,
# 1 equal win of user
# -1 equal win of comp

game = {
    "r": {
        "r": 0,
        "s": 1,
        "p": -1,
    },
    "s": {
        "r": -1,
        "s": 0,
        "p": 1,
    },
    "p": {
        "r": 1,
        "s": -1,
        "p": 0,
    },
}


def eval_game(player1, player2):
    """Evaluates the game."""
    return game[player1][player2]


def get_comp_choice():
    """Return comp choice"""
    return random.choice(list(game.keys()))


def get_user_choice():
    """

    :return: user choice from keys
    :rtype: int | None
    """

    user_choice = input("Choose form {}: ".format(list(game.keys()))).strip().lower()
    # return user_choice if user_choice in game.keys() else None --> another notation
    if user_choice in game.keys():
        result = user_choice
    else:
        result = None
    return result


if __name__ == '__main__':
    while True:
        user = get_user_choice()
        if user:  # when user makes his choice, pc makes his choice by random
            pc = get_comp_choice()
            result = eval_game(user, pc)  # assignment of choices into result for subsequent processing

            # result evaluation
            if result == 0:
                print("Tie!")
            elif result == 1:
                print("You won!")
            else:
                print("Computer won!")
