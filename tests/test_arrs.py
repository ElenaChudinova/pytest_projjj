from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([-1, -2, -3], 1, "test") == -2
    assert arrs.get([50.5, 55.1, 60.3], 1, "test") == 55.1
    assert arrs.get(['a', 'b', 'c'], 2, "test") == 'c'
    assert arrs.get([-1, -2, -3], -2, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, -3, -2, -1], 1) == [2, 3, -3, -2, -1]
    assert arrs.my_slice([1, 2, 3], 1, -1) == [2]
    assert arrs.my_slice([1, 2, 3, -3, -2, -1], 1, -2) == [2, 3, -3]
    assert arrs.my_slice([], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4], None, 0) == []
