from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("g/h")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
