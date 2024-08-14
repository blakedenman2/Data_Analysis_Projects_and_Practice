from working.working import convert
import pytest


def test_convert_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1 PM to 5 AM") == "13:00 to 05:00"
    with pytest.raises(ValueError):
        convert("5am to 8pm")
    with pytest.raises(ValueError):
        convert("5:00am to 6:00 PM")
    with pytest.raises(ValueError):
        convert("7:00 AM to 9:00  AM")


def test_convert_strings():
    assert convert("8 AM to 6 PM") == "08:00 to 18:00"
    with pytest.raises(ValueError):
        convert("12 o'clock")
    with pytest.raises(ValueError):
        convert("nine to five")


def test_convert_forget_to():
    with pytest.raises(ValueError):
        convert("9 AM - 4 PM")
    with pytest.raises(ValueError):
        convert("10 AM 5 PM")
    with pytest.raises(ValueError):
        convert("2:00 AM 3:00 PM")


def test_convert_values():
    assert convert("9:00 AM to 10:00 AM") == "09:00 to 10:00"
    assert convert("2:00 AM to 11:00 PM") == "02:00 to 23:00"
    assert convert("3:30 AM to 4:56 PM") == "03:30 to 16:56"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_convert_out_of_range():
    with pytest.raises(ValueError):
        convert("5:63 AM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("5:000 AM to 6:00 PM")
    with pytest.raises(ValueError):
        convert("2:90 AM 11:18 PM")
    with pytest.raises(ValueError):
        convert("222:00 AM to 14:00 PM")
    with pytest.raises(ValueError):
        convert("2:00 AM to 91:00 PM")
    with pytest.raises(ValueError):
        convert("27:00 AM to 11:00 PM")
