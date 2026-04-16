import pytest
from numb3rs import validate

def test_ip():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("12.52.512.512") == False
    assert validate("90cat") == False

