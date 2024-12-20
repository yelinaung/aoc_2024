"""
https://adventofcode.com/2024/day/2
"""

from typing import List


def prepare_data(file_name: str):
    with open(file_name) as f:
        return [list(map(int, L.strip().split())) for L in f.readlines()]


def valid_sequence(nums: List[int]) -> bool:
    # empty list or a list with only 1 item -> valid
    if not nums or len(nums) < 2:
        return True

    direction: bool | None = None
    for i in range(len(nums) - 1):
        # diff between next item and the current
        diff = nums[i + 1] - nums[i]
        # invalid if the diff is between 1 and 3
        if not (1 <= abs(diff) <= 3):
            return False

        current_direction = diff > 0
        if direction is None:
            direction = current_direction
        elif direction != current_direction:
            return False

    return True


def can_make_valid_sequence(nums: List[int]):
    if valid_sequence(nums):
        return True

    return any(valid_sequence(nums[:i] + nums[i + 1 :]) for i in range(len(nums)))


def part_1(file_name: str) -> int:
    data = prepare_data(file_name)
    return sum(1 if valid_sequence(nums) else 0 for nums in data)


def part_2(file_name: str) -> int:
    data = prepare_data(file_name)
    return sum(1 if can_make_valid_sequence(nums) else 0 for nums in data)


def test_part_1():
    assert part_1("day_02/sample.txt") == 2
    print(part_1("day_02/data.txt"))


def test_part_2():
    assert part_2("day_02/sample.txt") == 4
    print(part_2("day_02/data.txt"))
