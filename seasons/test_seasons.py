from seasons import minutes
import pytest

def test_minutes():
    assert minutes(2024, 2, 9) == "Five hundred twenty-seven thousand forty minutes"
    assert minutes(2023, 2, 9) == "One million, fifty-two thousand, six hundred forty minutes"

