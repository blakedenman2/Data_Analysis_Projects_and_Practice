from twttr import shorten


def test_lowercase():
    assert shorten("beans") == "bns"
    assert shorten("good day sir") == "gd dy sr"


def test_uppercase():
    assert shorten("How ARE yoU?") == "Hw R y?"
    assert shorten("I'M NOT yeLLIng!") == "'M NT yLLng!"


def test_numbers():
    assert shorten("t3st1ng") == "t3st1ng"
    assert shorten("I hav3 13 B4n4n45") == " hv3 13 B4n4n45"


def test_specials():
    assert shorten("-+;45dftaaaer5?/") == "-+;45dftr5?/"
    assert shorten("1 ___ 2_   >") == "1 ___ 2_   >"
