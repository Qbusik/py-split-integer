import pytest

from app.split_integer import split_integer

@pytest.mark.parametrize(
    "value,parts,result",
    [
        (8, 1, [8]),
        (1, 4, [0, 0, 0, 1]),
        (0, 5, [0, 0, 0, 0]),
        (6, 2, [3, 3]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(value, parts, result) -> None:
    assert sum(split_integer(value, parts)) == sum(result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts(value, parts, result) -> None:
    if value % parts == result:
        assert all(split_integer(value, parts))


def test_should_return_part_equals_to_value_when_split_into_one_part(value, parts, result) -> None:
    if parts == 1:
        assert split_integer(value, parts) == result


def test_parts_should_be_sorted_when_they_are_not_equal(value, parts, result) -> None:
    assert sorted(split_integer(value, parts)) == result


def test_should_add_zeros_when_value_is_less_than_number_of_parts(value, parts, result) -> None:
    if value < parts:
        assert split_integer(value, parts) == result
