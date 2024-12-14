import sys
import math
import re

from collections import defaultdict

lines = [line for line in sys.stdin.read().splitlines()]

grid = defaultdict(list)

for i, line in enumerate(lines):
    x, y, dx, dy = map(int, re.findall(r"-?\d+", line))
    grid[x, y].append((dx, dy))

W = 101
H = 103
current = grid
for it in range(10**6):
    if it == 100:
        quad = [0] * 4
        for (x, y), robots in current.items():
            mx = W // 2
            my = H // 2
            if x > mx and y < my:
                quad[0] += len(robots)
            elif x < mx and y < my:
                quad[1] += len(robots)
            elif x < mx and y > my:
                quad[2] += len(robots)
            elif x > mx and y > my:
                quad[3] += len(robots)

        print("Part 1:", math.prod(quad))

    if all(len(v) == 1 for v in current.values()):
        print("Part 2:", it)
        break

    new_grid = defaultdict(list)
    for (x, y), robots in current.items():
        for dx, dy in robots:
            nx = (x + dx) % W
            ny = (y + dy) % H
            new_grid[nx, ny].append((dx, dy))

    current = new_grid
