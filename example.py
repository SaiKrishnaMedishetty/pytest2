import math
import pytest

@pytest.fixture
def input_value():
    input_value = 8
    return input_value

def test_add(input_value):
    assert input_value + 2 == 1
