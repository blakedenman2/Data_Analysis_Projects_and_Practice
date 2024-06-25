from plates import is_valid


def test_first_two_are_letters():
    assert is_valid("TG22") == True
    assert is_valid("3T4T") == False
    assert is_valid("R57TT") == False
    assert is_valid("7777") == False
    assert is_valid("89") == False


def test_size_is_2to6():
    assert is_valid("HK") == True
    assert is_valid("P") == False
    assert is_valid("PLTY3434585929827985") == False
    assert is_valid("RT66666") == False


def test_numbers_at_end():
    assert is_valid("VB5555") == True
    assert is_valid("SD55UI") == False
    assert is_valid("QWWEE4") == True
    assert is_valid("EW2RT") == False


def test_valid_characters():
    assert is_valid("RE45") == True
    assert is_valid("SSS$$") == False
    assert is_valid("PO40`]") == False
    assert is_valid("EL7<>") == False


def test_first_num_not_zero():
    assert is_valid("SX45") == True
    assert is_valid("SX045") == False
