import re

mul_re = re.compile(r"mul\((\d+),\s*(\d+)\)")
control_re = re.compile(r"don\'t\(\)|do\(\)")


def part_1(file_name: str) -> int:
    total = 0
    with open(file_name) as f:
        for line in f:
            for match in mul_re.finditer(line.strip()):
                x, y = map(int, match.groups())
                total += x * y
    return total


def part_2(file_name: str) -> int:
    total = 0
    line = None
    with open(file_name) as f:
        line = " ".join(f.readlines())

    evaluating = True
    last_end = 0
    for part in control_re.finditer(line):
        if evaluating:
            for mul_match in mul_re.finditer(line[last_end : part.start()]):
                x, y = map(int, mul_match.groups())
                total += x * y
        if part.group() == "don't()":
            evaluating = False
        elif part.group() == "do()":
            evaluating = True
        last_end = part.end()

    if evaluating:
        for mul_match in mul_re.finditer(line[last_end:]):
            x, y = map(int, mul_match.groups())
            total += x * y

    return total


def test_part_1():
    assert part_1("day_03/sample.txt") == 161
    print(f'\nPart 1 {part_1("day_03/data.txt")}')


def test_part_2():
    assert part_2("day_03/sample2.txt") == 48
    print(f'\nPart 2 {part_2("day_03/data.txt")}')
