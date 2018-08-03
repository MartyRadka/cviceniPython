from circle2 import get_circumference, get_area_of_circle


def test_get_circumference():
    assert get_circumference(3.4) == 21.362830044410593
    assert get_circumference(3) == 18.84955592153876
    assert not get_circumference(0)
    assert not get_circumference(-3.4)


def test_get_area_of_circle():
    assert get_area_of_circle(1.4) == 6.157521601035993
    assert get_area_of_circle(1) == 3.141592653589793
    assert not get_area_of_circle(0)
    assert not get_area_of_circle(-1.4)
