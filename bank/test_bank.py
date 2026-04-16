from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("Hay") == 20
    assert value("what") == 100
    assert value("How") == 20
    assert value("Good morning") == 100

