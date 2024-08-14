from bank import value


def test_is_hello():
    assert value("hello") == 0


def test_starts_with_h():
    assert value("howdy") == 20
    assert value("HEY") == 20
    assert value("how are ya") == 20


def test_everything_else():
    assert value("a    HHWhjdj") == 100
    assert value("qWWERT1234 QE24") == 100
    assert value(",../';I24K 7--- HHHH") == 100
