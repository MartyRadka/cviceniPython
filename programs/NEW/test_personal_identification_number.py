import pytest

from personal_identification_number import is_pin_correct, is_divisible_by_11, \
    get_day_of_birth, get_gender

# pin = personal identification number


def test_is_pin_correct():
    assert is_pin_correct("876207/4772")  # pin correct
    assert not is_pin_correct("")  # no pin
    assert not is_pin_correct("8762074772")  # no slash in pin
    assert not is_pin_correct("876207/477")  # pin too short  --> this test doesn't work!!!
    assert not is_pin_correct("876207/47721")  # pin too long
    assert not is_pin_correct("876207/477x")  # letter after slash
    assert not is_pin_correct("87620x/4772")  # letter before slash
    assert not is_pin_correct("87620/74772")  # incorrect position of slash


def test_is_divisible_by_11():
    assert is_divisible_by_11("876207/4772")  # is divisible by 11
    assert not is_divisible_by_11("876207/4771")  # not divisible by 11


def test_get_day_of_birth():
    with pytest.raises(ValueError):
        get_day_of_birth("879207/4772")  # bad value for month

    with pytest.raises(ValueError):
        get_day_of_birth("876242/4772")  # bad value for day


def test_get_gender():
    assert get_gender("876207/4772")  # correct pin for woman
    assert get_gender("810407/1822")  # correct pin for man
    assert not get_gender("877207/4772")  # incorrect pin for woman
    assert not get_gender("818407/1822")  # incorrect pin for man












