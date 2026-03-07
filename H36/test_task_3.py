import pytest
from functions import multiply_list_by_7

@pytest.mark.parametrize("list_nums, should_return",[
    ([1,2,3,4,5], [7,14,21,28,35]),
    ([0,-1,0.5], [0,-7,3.5]),
    ([],[])
])
def test_list_multiply(list_nums: list, should_return: list)-> bool:
    result = multiply_list_by_7(list_nums)
    assert result == should_return