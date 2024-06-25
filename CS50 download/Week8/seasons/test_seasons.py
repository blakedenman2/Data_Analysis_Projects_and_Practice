from seasons import Seconds
from datetime import datetime, date, timedelta
import pytest

tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
one_year_away = (date.today() + timedelta(days=365)).strftime("%Y-%m-%d")

def test_seasons_init():
    instance = Seconds(tomorrow)
    assert instance.birth_date == date.fromisoformat(tomorrow)
    assert instance.today == date.today()
    assert instance.time_difference == 1
    assert instance.total_minutes == 1440
    with pytest.raises(SystemExit):
        Seconds("2024,10,10")
    with pytest.raises(SystemExit):
        Seconds("10/18/1995")


def test_seasons_str():
    instance = Seconds(tomorrow)
    assert str(instance) == "One thousand, four hundred forty minutes"
    instance2 = Seconds(one_year_away)
    assert str(instance2) == "Five hundred twenty-five thousand, six hundred minutes"
