import sys
import itertools

# fmt: off
sys.path.append("../..")
from lib.list import *
# fmt: on

lines = [line for line in sys.stdin.read().splitlines()]


empty_rows = set()
empty_cols = set()
galaxies = []
for y, line in enumerate(lines):
    if all(c == "." for c in line):
        empty_rows.add(y)
        continue

    for x, c in enumerate(line):
        if c == "#":
            galaxies.append((x, y))


for x, line in enumerate(transpose(lines)):
    if all(c == "." for c in line):
        empty_cols.add(x)

pairs = list(itertools.combinations(galaxies, 2))


def calc(factor):
    total = 0

    for (x1, y1), (x2, y2) in pairs:
        dist = abs(y2 - y1) + abs(x2 - x1)
        xexp = sum(
            factor - 1
            for x in range(min(x1, x2) + 1, max(x1, x2))
            if x in empty_cols
        )
        yexp = sum(
            factor - 1
            for y in range(min(y1, y2) + 1, max(y1, y2))
            if y in empty_rows
        )

        total += dist + xexp + yexp

    return total


print("Part 1:", calc(2))
print("Part 2:", calc(10**6))
