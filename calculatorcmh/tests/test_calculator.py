from calculatorcmh import calculator


def test_sum():
    act = calculator.sum(3)
    exp = 6
    assert act == exp, "Sum not calculated as expected"


def test_sqr():
    act = calculator.sqr(3)
    exp = 9
    assert act == exp, "Square not calculated as expected"


def test_cube():
    act = calculator.cube(3)
    exp = 27
    assert act == exp, "Cube not calculated as expected"


def test_name():
    act = calculator.name(3)
    exp = "Three"
    assert act == exp, "Name not translated as expected"


def test_name_outofrange():
    act = calculator.name(300)
    exp = "To be added"
    assert act == exp, "Name not translated as expected"
