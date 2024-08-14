from um.um import count


def test_count_reg_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count(" um ") == 1
    assert count("um um UM") == 3


def test_count_um_words():
    assert count("yummy") == 0
    assert count("Umame") == 0
    assert count(" gum ") == 0
    assert count("glum summer SHWUM") == 0


def test_count_sentences():
    assert count("Yummy in my tummy") == 0
    assert count("Um, can I have an umpire?") == 1
    assert count("Um.... well, um! ") == 2
    assert count("Instrumental gum is... um... cool.") == 1
