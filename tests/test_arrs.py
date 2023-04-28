import pytest

from utils import arrs


@pytest.fixture
def fixture_array():
    return [1, 2, 3, 4]


@pytest.mark.parametrize('list, index, default, value', [
    ([1, 2, 3], 1, "test", 2),
    ([1, 2, 3], 2, "test", 3),
    ([1, 2, 3], 3, "test", "test"),
    ([], 0, "test", "test"),
    ([1, 2, 3], -1, "test", "test"),
])
def test_get(list, index, default, value):
    assert arrs.get(list, index, default) == value


def test_slice(fixture_array):
    assert arrs.my_slice(fixture_array, 1, 3) == [2, 3]
    assert arrs.my_slice(fixture_array, 1) == [2, 3, 4]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(fixture_array, -1) == [4]
    assert arrs.my_slice(fixture_array, - 5) == fixture_array
