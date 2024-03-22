from fuel import convert, gauge
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_correct_input():
    assert convert("1/4") == 25, "Fraction '1/4' should convert to 25%"
    assert gauge(25) == "25%", "25 should gauge as '25%'"
    assert convert("1/100") == 1, "Fraction '1/100' should convert to 1%"
    assert gauge(1) == "E", "1 should gauge as 'E'"
    assert convert("99/100") == 99, "Fraction '99/100' should convert to 99%"
    assert gauge(99) == "F", "99 should gauge as 'F'"