import re

filter_re = r"mul\(\d+,\d+\)"
mul_re = re.compile(r"mul\((\d+),\s*(\d+)\)")


def part_1(file_name: str) -> int:
    with open(file_name) as f:
        total = 0
        data = " ".join([line.strip() for line in f.readlines()])
        matches = re.finditer(filter_re, data, re.MULTILINE)
        for m in matches:
            # let there be warlus!
            if match := mul_re.match(m.group()):
                x, y = map(int, match.groups())
                total += x * y

    return total


def test_part_1():
    assert part_1("day_03/sample.txt") == 161
    print(part_1("day_03/data.txt"))
