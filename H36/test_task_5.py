import pytest
from functions import is_positive_num

@pytest.mark.parametrize("num, expected", [
    (1, True),
    (1000, True),
    (0, True),
])
def test_is_positive_num_successfull(num, expected):
    assert is_positive_num(num) == expected

@pytest.mark.parametrize("negative_num", [
    (-1),
    (-151),
    (-0.0001),
])
def test_is_positive_num_raises_error(negative_num):
    with pytest.raises(ValueError) as excinfo:
        is_positive_num(negative_num)