import re

filter_re = r"mul\(\d+,\d+\)"
mul_re = re.compile(r"mul\((\d+),\s*(\d+)\)")


def part_1(file_name: str) -> int:
    total = 0
    with open(file_name) as f:
        for line in f:
            for match in mul_re.finditer(line.strip()):
                x, y = map(int, match.groups())
                total += x * y
    return total


def test_part_1():
    assert part_1("day_03/sample.txt") == 161
    print(part_1("day_03/data.txt"))
