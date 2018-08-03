import mock

from cviceni_python_git.games.rock_paper_dict import eval_game, get_comp_choice, get_user_choice


def test_eval_game():
    assert eval_game("r", "r") == 0  # Tie
    assert eval_game("s", "r") == -1  # -1 equal win of comp
    assert eval_game("p", "r") == 1  # 1 equal win of user


def test_get_comp_choice():
    assert get_comp_choice() in ["r", "s", "p"]  # choice is in dict game


@mock.patch('builtins.input', return_value="r")  #
def test_get_user_choice_valid_value(mock_input):  # in mock value Return the function how it was called with its parameters
    assert get_user_choice() == "r"


@mock.patch('builtins.input', return_value="bla")
def test_get_user_choice_invalid_value(mock_input):
    assert get_user_choice() is None






    # assert not eval_game(" ", "r") is None
    # assert not eval_game(4, "p") is None
    # assert not eval_game("bla", "s") is None

