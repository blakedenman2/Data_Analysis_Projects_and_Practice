from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("1/10000") == 0
    assert convert("100/100") == 100
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("20/4")
    with pytest.raises(ValueError):
        convert("cat/6")
    with pytest.raises(ValueError):
        convert("7/ten")


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
