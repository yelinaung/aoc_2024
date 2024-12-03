"""
https://adventofcode.com/2024/day/2
"""

from typing import List


def prepare_data(file_name: str):
    with open(file_name) as f:
        return [list(map(int, L.strip().split())) for L in f.readlines()]


def valid_sequence(nums: List[int]) -> bool:
    if not nums or len(nums) < 2:
        return True

    direction: bool | None = None
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if not (1 <= abs(diff) <= 3):
            return False

        current_direction = diff > 0
        if direction is None:
            direction = current_direction
        elif direction != current_direction:
            return False

    return True


def problem_damper(nums: List[int]):
    if valid_sequence(nums):
        return True

    for i in range(len(nums)):
        if valid_sequence(nums[:i] + nums[i + 1 :]):
            return True

    return False


def part_1(file_name: str) -> int:
    data = prepare_data(file_name)
    return sum(1 if valid_sequence(nums) else 0 for nums in data)


def part_2(file_name: str) -> int:
    data = prepare_data(file_name)
    return sum(1 if problem_damper(nums) else 0 for nums in data)


def test_part_1():
    assert part_1("day_02/sample.txt") == 2
    print(part_1("day_02/data.txt"))


def test_part_22():
    assert part_2("day_02/sample.txt") == 4
    print(part_2("day_02/data.txt"))
