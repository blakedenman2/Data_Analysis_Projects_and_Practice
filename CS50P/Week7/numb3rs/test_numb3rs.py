from numb3rs.numb3rs import validate


def test_validate_format():
    assert validate("233.34.5.174") == True
    assert validate("1.2.3.4") == True
    assert validate("000.000.000.000") == True
    assert validate("5.34.23.21.42") == False
    assert validate("234.0.2.3.4") == False
    assert validate("4.5") == False
    assert validate("45") == False
    assert validate("0,4.3.5.66") == False
    assert validate("2333455574") == False


def test_validate_chars():
    assert validate("cat") == False
    assert validate("34.efg.55.0") == False
    assert validate("$.34.'`.dog") == False


def test_validate_255():
    assert validate("233.34.5.174") == True
    assert validate("2.4.77.900") == False
    assert validate("233.34.555.74") == False
    assert validate("20.54.77.00") == True
    assert validate("2303.34.555.74") == False
