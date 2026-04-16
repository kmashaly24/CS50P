from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar(20)
    with pytest.raises(ValueError):
        jar1.deposit(21)


def test_withdraw():
    jar2 = Jar(20)
    with pytest.raises(ValueError):
        jar2.withdraw(10)
