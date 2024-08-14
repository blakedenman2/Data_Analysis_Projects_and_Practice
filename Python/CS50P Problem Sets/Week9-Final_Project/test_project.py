from project import check_wind, check_windns, check_windri
from project import check_wave, check_waveri
import pandas as pd

data = {
    "HR": [10, 9, 8, 7, 6, 5],
    "MIN": [50, 50, 50, 50, 50, 50],
    "WVHT": [2.0, 1.6, 2.0, 2.0, 2.0, 1.6],
    "APD": [3.1, 3.0, 3.1, 3.0, 3.0, 3.0],
    "MWD": [298, 315, 303, 336, 4, 346],
    "WSPD": [17.9, 15.7, 15.7, 17.9, 17.9, 15.7],
    "WDIR": [300, 310, 320, 320, 320, 330]
}

data2 = {
    "HR": [10, 9, 8, 7, 6, 5],
    "MIN": [50, 50, 50, 50, 50, 50],
    "WVHT": [4.0, 3.6, 4.0, 4.0, 4.0, 3.6],
    "APD": [8.1, 8.0, 8.1, 8.0, 8.0, 8.0],
    "MWD": [90, 100, 103, 80, 104, 95],
    "WSPD": [17.9, 15.7, 15.7, 17.9, 17.9, 15.7],
    "WDIR": [300, 310, 320, 320, 320, 330]
}

data3 = {
    "HR": [10, 9, 8, 7, 6, 5],
    "MIN": [50, 50, 50, 50, 50, 50],
    "WVHT": [1.0, 0.6, 1.0, 1.0, 1.0, 0.6],
    "APD": [3.1, 3.0, 3.1, 3.0, 3.0, 3.0],
    "MWD": [90, 100, 103, 80, 104, 95],
    "WSPD": [12.9, 10.7, 11.7, 14.9, 12.9, 10.7],
    "WDIR": [200, 210, 220, 220, 220, 230]
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)


def test_check_wind():
    assert check_wind(df) == "Clean, but windy"
    assert check_wind(df2) == "Clean, but windy"
    assert check_wind(df3) == "Sideshore, but should be manageable"


def test_check_windns():
    assert check_windns(df) == "Clean, but windy"
    assert check_windns(df2) == "Clean, but windy"
    assert check_windns(df3) == "Doesn't look great"


def test_check_windri():
    assert check_windri(df) == "Clean, but windy"
    assert check_windri(df2) == "Clean, but windy"
    assert check_windri(df3) == "Doesn't look great"


def test_check_wave():
    assert check_wave(df) == "Wave direction points to waves being poor"
    assert check_wave(df2) == "Looks good for a midlength!"
    assert check_wave(df3) == "Too small"


def test_check_waveri():
    assert check_waveri(df) == "Wave direction points to waves being poor"
    assert check_waveri(df2) == "Looks good for a midlength!"
    assert check_waveri(df3) == "Too small"
