import re

regex = r"mul\(\d+,\d+\)"


def part_1(file_name: str) -> int:
    with open(file_name) as f:
        total = 0
        data = " ".join([L.strip() for L in f.readlines()])
        matches = re.finditer(regex, data, re.MULTILINE)
        for m in matches:
            match = re.match(r"mul\((\d+),\s*(\d+)\)", m.group())
            if match:
                x, y = map(int, match.groups())
                total += x * y

    return total


def test_part_1():
    assert part_1("day_03/sample.txt") == 161
    print(part_1("day_03/data.txt"))
