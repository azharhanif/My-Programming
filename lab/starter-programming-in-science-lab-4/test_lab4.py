import unittest
from Lab4 import check_weekday_or_weekend, get_day_name

# Test check_weekday_or_weekend function
def test_check_weekday_or_weekend():
    assert check_weekday_or_weekend(0) == "Not a proper day number!"
    assert check_weekday_or_weekend(2) == "It is a Weekday!"
    assert check_weekday_or_weekend(5) == "It is a Weekday!"
    assert check_weekday_or_weekend(6) == "It is a Weekend!"
    assert check_weekday_or_weekend(7) == "It is a Weekend!"
    assert check_weekday_or_weekend(8) == "Not a proper day number!"

# Test get_day_name function
def test_get_day_name():
    assert get_day_name(0) == "Not a proper day number!"
    assert get_day_name(1) == "It is a Monday!"
    assert get_day_name(2) == "It is a Tuesday!"
    assert get_day_name(3) == "It is a Wednesday!"
    assert get_day_name(4) == "It is a Thursday!"
    assert get_day_name(5) == "It is a Friday!"
    assert get_day_name(6) == "It is a Saturday!"
    assert get_day_name(7) == "It is a Sunday!"
    assert get_day_name(8) == "Not a proper day number!"

# Run tests
if __name__ == '__main__':
    test_check_weekday_or_weekend()
    test_get_day_name()
    print("All tests passed!")
