import pytest

from utils.dicts import get_val

SOME_DICT = {"cat": "Мурзик", "dog": "Шарик"}


def test_get_val():
    assert get_val(SOME_DICT, "cat", "Не найдено") == "Мурзик"
    assert get_val(SOME_DICT, "dog", "Не найдено") == "Шарик"
    assert get_val(SOME_DICT, "bat", "Не найдено") == "Не найдено"
    assert get_val(SOME_DICT, "cow") == "Животное"
