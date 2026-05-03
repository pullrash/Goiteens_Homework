import pytest
from functions import is_palindrom, word_upper
@pytest.mark.parametrize("word, should_return", [
    ("hello", "HELLO"),
    ("helLo", "HELLO"),
    ("HEllO", "HELLO"),
    ("HELLO", "HELLO")
])
def test_is_word_upper(word:str, should_return: str)-> bool:
    result = word_upper(word)
    assert result == should_return

@pytest.mark.parametrize("word, should_return", [
    ("hello", False),
    ("lol", True),
    ("did", True),
    ("hello", False),
])
def test_is_palindrom(word:str, should_return: bool)-> bool:
    result = is_palindrom(word)
    assert result == should_return