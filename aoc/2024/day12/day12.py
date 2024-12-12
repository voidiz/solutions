import sys

from collections import defaultdict

lines = sys.stdin.read().splitlines()
grid = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x, y] = c

p1 = 0
p2 = 0
vis = set()
for sx, sy in grid:
    if (sx, sy) in vis:
        continue

    s = [(sx, sy)]
    perim = defaultdict(set)
    area = 0

    while s:
        x, y = s.pop()
        if (x, y) in vis:
            continue

        vis.add((x, y))
        area += 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if (nx, ny) in grid and grid[x, y] == grid[nx, ny]:
                s.append((nx, ny))
            else:
                perim[nx, ny].add((dx, dy))

    p1 += area * sum(len(p) for p in perim.values())

    sides = 0
    for (px, py), deltas in list(perim.items()):
        for d in deltas:
            right = (px + 1, py)
            below = (px, py + 1)
            if d not in (perim[right] | perim[below]):
                sides += 1

    p2 += area * sides

print("Part 1:", p1)
print("Part 2:", p2)
