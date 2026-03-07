import pytest
from functions import plus, minus, division, multiply


@pytest.mark.parametrize("num_1, num_2, should_equals", [
    (15, 10, 25),
    (1.4, 10, 11.4),
    (1.4, 45.2, 46.6),
    (15, 0, 15),
    (0, 10, 10),
    (-91, 10, -81),
    (15, -15, 0)
])
def test_arefmetic_operation_plus(num_1: float, num_2: float, should_equals: float)-> bool:
    result = plus(num_1, num_2)
    assert result == should_equals


@pytest.mark.parametrize("num_1, num_2, should_equals", [
    (15, 10, 5),
    (1.4, 10, -8.6),
    (1.4, 45.2, 1.4 - 45.2),
    (15, 0, 15),
    (0, 10, -10),
    (-91, 10, -101),
    (15, -15, 30)
])
def test_arefmetic_operation_minus(num_1: float, num_2: float, should_equals: float)-> bool:
    result = minus(num_1, num_2)
    assert result == should_equals


@pytest.mark.parametrize("num_1, num_2, should_equals", [
    (15, 10, 15/10),
    (1.4, 10, 1.4/10),
    (1.4, 45.2, 1.4/45.2),
    (15, 0, 0),
    (0, 10, 0/10),
    (-91, 10, -91/10),
    (15, -15, 15/-15)
])
def test_arefmetic_operation_devision(num_1: float, num_2: float, should_equals: float)-> bool:
    try:
        result = division(num_1, num_2)
        assert result == should_equals
    except ZeroDivisionError:
        pass


@pytest.mark.parametrize("num_1, num_2, should_equals", [
    (15, 10, 15*10),
    (1.4, 10, 1.4*10),
    (1.4, 45.2, 1.4*45.2),
    (15, 0, 15*0),
    (0, 10, 0*10),
    (-91, 10, -91*10),
    (15, -15, 15*-15)
])
def test_arefmetic_operation_multiply(num_1: float, num_2: float, should_equals)-> bool:
    result = multiply(num_1, num_2)
    assert result == should_equals