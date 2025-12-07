import sys
import functools

lines = [line for line in sys.stdin.read().splitlines()]

x = y = 0
for i, c in enumerate(lines[0]):
    if c == "S":
        x = i


def p1(x, y, vis):
    if (x, y) in vis:
        return 0

    vis.add((x, y))
    if y >= len(lines):
        return 0

    if lines[y][x] == "^":
        return 1 + p1(x - 1, y, vis) + p1(x + 1, y, vis)

    return p1(x, y + 1, vis)


@functools.cache
def p2(x, y):
    if y >= len(lines):
        return 1

    if lines[y][x] == "^":
        return p2(x - 1, y) + p2(x + 1, y)

    return p2(x, y + 1)


print("Part 1:", p1(x, y, set()))
print("Part 2:", p2(x, y))
