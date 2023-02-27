import sys
import math
import re

grid, path = (line for line in sys.stdin.read().split("\n\n"))
grid = grid.splitlines()

g = {}
start = None
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c in ["#", "."]:
            if not start:
                start = (j, i)
            g[(j, i)] = c

assert start
steps = list(map(int, re.findall(r"\d+", path)))
dirs = re.findall(r"L|R", path)


def next_a(start, dx, dy):
    sx, sy = start
    if dx == 1:
        minx = math.inf
        for x, y in g.keys():
            if y == sy and x < minx:
                minx = x
        return minx, sy, dx, dy
    elif dy == 1:
        miny = math.inf
        for x, y in g.keys():
            if x == sx and y < miny:
                miny = y
        return sx, miny, dx, dy
    elif dx == -1:
        maxx = 0
        for x, y in g.keys():
            if y == sy and x > maxx:
                maxx = x
        return maxx, sy, dx, dy
    else:
        assert dy == -1
        maxy = 0
        for x, y in g.keys():
            if x == sx and y > maxy:
                maxy = y
        return sx, maxy, dx, dy


def next_b(start, dx, dy):
    """
    y:                          x:
         AB     0 - 49              FE      0 - 49
         C      50 - 99              DCA    50 - 99
        ED      100 - 149              B    100 - 149
        F       150 - 199

        A           E
      E C B       A F D
        D           B

    A:
        - E: dx = -1, x = 50 -> dx = 1, x = 0, y = 149 - prevy
        - F: dy = -1, y = 0 -> dx = 1, x = 0, y = prevx + 100
    B:
        - C: dy = 1, y = 49 -> dx = -1, x = 99, y = prevx - 50
        - F: dy = -1, y = 0 -> dy = -1, x = prevx - 100, y = 199
        - D: dx = 1, x = 149 -> dx = -1, x = 99, y = 149 - prevy
    C:
        - E: dx = -1, x = 50 -> dy = 1, x = prevy - 50, y = 100
        - B: dx = 1, x = 99 -> dy = -1, x = 99 + (prevy - 50), y = 49
    D:
        - B: dx = 1, x = 99 -> dx = -1, x = 149, y = 49 - (prevy - 100)
        - F: dy = 1, y = 149 -> dx = -1, x = 49, y = prevx + 100
    E:
        - C: dy = -1, y = 100 -> dx = 1, x = 49, y = prevx + 50
        - A: dx = -1, x = 0 -> dx = 1, x = 49, y = 149 - prevy
    F:
        - D: dx = 1, x = 49 -> dy = -1, x = 49 + (prevy - 150), y = 149
        - B: dy = 1, y = 199 -> dy = 1, x = prevx + 100, y = 0
        - A: dx = -1, x = 0 -> dy = 1, x = 49 + prevy - 150, y = 0
    """

    x, y = start
    if dx == 1:
        if x == 49:
            return 50 + (y - 150), 149, 0, -1
        if x == 149:
            return 99, 149 - y, -1, 0
        if x == 99:
            if y < 100:
                return 100 + (y - 50), 49, 0, -1
            return 149, 49 - (y - 100), -1, 0
    elif dy == 1:
        if y == 49:
            return 99, x - 50, -1, 0
        if y == 149:
            return 49, x + 100, -1, 0
        if y == 199:
            return x + 100, 0, 0, 1
    elif dx == -1:
        if x == 50:
            if y < 50:
                return 0, 149 - y, 1, 0
            return y - 50, 100, 0, 1
        if x == 0:
            if y < 150:
                return 50, 149 - y, 1, 0
            return y - 100, 0, 0, 1
    else:
        assert dy == -1
        if y == 0:
            if x < 100:
                return 0, x + 100, 1, 0
            return x - 100, 199, 0, -1
        if y == 100:
            return 50, x + 50, 1, 0

    assert False and "unreachable"


def solve(start, next_fn):
    dx, dy = 1, 0
    for i in range(len(steps)):
        step = steps[i]
        for j in range(step):
            j = j + 1
            x, y = start
            next = x + dx, y + dy
            if next in g:
                if g[next] == "#":
                    break

                start = next
                continue

            nx, ny, ndx, ndy = next_fn(start, dx, dy)
            if g[(nx, ny)] != "#":
                start = (nx, ny)
                dx, dy = ndx, ndy
                continue

            break

        if i < len(steps) - 1:
            dir = dirs[i]
            if dir == "L":
                dx, dy = dy, -dx
            else:
                dx, dy = -dy, dx

    x, y = [c + 1 for c in start]
    facing = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}[(dx, dy)]
    return 1000 * y + 4 * x + facing


print("Part 1:", solve(start, next_a))
print("Part 2:", solve(start, next_b))
