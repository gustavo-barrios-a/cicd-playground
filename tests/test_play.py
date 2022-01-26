import numpy as np
import pytest
from playground.play import findMaxCrossing
from playground.play import findMaxSubarray
from playground.play import get_json
from playground.play import merge_sort


def test_get_json(mock_response):
    result = get_json("http://fakeurl")
    assert result["mock_key"] == "mock_response"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([2, 4, 5, 7, 1, 2, 3, 6], [1, 2, 2, 3, 4, 5, 6, 7]),
        ([122, 52333, 0, 31, 42, 4, 89], [0, 4, 31, 42, 89, 122, 52333]),
    ],
)
def test_merge_sort(test_input, expected):
    merge_sort(test_input)
    assert test_input == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            np.array(
                [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
            ),
            (7, 10, 43),
        )
    ],
)
def test_findmax(test_input, expected):
    res1 = findMaxCrossing(test_input, 0, 7, 15)
    res2 = findMaxSubarray(test_input, 0, 15)
    assert res1 == res2 == expected
