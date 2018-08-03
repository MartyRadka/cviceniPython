from circle import get_circumference, get_area_of_circle


def test_get_circumference():
    assert get_circumference(3.4) == 21.362830044410593
    assert not get_circumference(3)
    assert not get_circumference(0)
    assert not get_circumference(-3)


def test_get_area_of_circle():
    assert get_area_of_circle(1.4) == 6.157521601035993
    assert not get_area_of_circle(1)
    assert not get_area_of_circle(0)
    assert not get_area_of_circle(-1.6)

