"""
https://adventofcode.com/2024/day/2
"""


def prepare_data(file_name: str):
    with open(file_name) as f:
        return [list(map(int, L.strip().split())) for L in f.readlines()]


def valid_sequence(nums) -> bool:
    direction = None
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if not (1 <= abs(diff) <= 3):
            return False
        if diff > 0:
            if direction == "decreasing":
                return False
            direction = "increasing"
        elif diff < 0:
            if direction == "increasing":
                return False
            direction = "decreasing"
        else:
            return False
    return True


def part_1(file_name):
    data = prepare_data(file_name)
    return sum(1 if valid_sequence(nums) else 0 for nums in data)


def test_part_1():
    assert part_1("day_02/sample.txt") == 2
    print(part_1("day_02/data.txt"))
