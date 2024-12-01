import sys
from collections import Counter

"""
To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!
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
