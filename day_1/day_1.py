import sys
from collections import Counter

"""
https://adventofcode.com/2024/day/1
"""

with open(sys.argv[1]) as f:
    data = [tuple(map(int, line.split())) for line in f]

# Part 1
left, right = zip(*data)
left, right = sorted(left), sorted(right)
print(sum([abs(L - R) for L, R in zip(left, right)]))

# Part 2
right = Counter(right)
print(sum([L * right.get(L, 0) for L in left]))
