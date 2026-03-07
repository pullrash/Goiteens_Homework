import pytest
from functions import sum_dict

@pytest.mark.parametrize("dict_1, dict_2, should_return", [
    ({"balance_1":15, "balance_2":1},
     {"balance_3":13},
     {"balance_1":15, "balance_2":1, "balance_3":13}),
    
    ({"balance_1":15, "balance_2":1},
     {"balance_2":13},
     {"balance_1":15, "balance_2":14}),
    
    ({"balance_1":15, "balance_2":1},
     {},
     {"balance_1":15, "balance_2":1}),
    
    ({},
     {"balance_3":13},
     {"balance_3":13}),
])
def test_sum_dict(dict_1: dict, dict_2: dict, should_return: dict)-> bool:
    result = sum_dict(dict_1, dict_2)
    assert result == should_return