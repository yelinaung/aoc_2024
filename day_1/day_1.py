from collections import Counter
from typing import Iterable


"""
https://adventofcode.com/2024/day/1
"""


def prepare_data(file_name: str) -> Iterable[tuple[int, ...]]:
    with open(file_name) as f:
        data = [tuple(map(int, line.split())) for line in f]
    return zip(*data)


def part_1(file_name: str) -> int:
    left, right = prepare_data(file_name)
    return sum([abs(L - R) for L, R in zip(sorted(left), sorted(right))])


def part_2(file_name: str) -> int:
    left, right = prepare_data(file_name)
    return sum([L * Counter(right).get(L, 0) for L in left])


def test_part_1():
    assert part_1("day_1/sample.txt") == 11

    print(part_1("day_1/data.txt"))


def test_part_2():
    assert part_2("day_1/sample.txt") == 31

    print(part_2("day_1/data.txt"))
