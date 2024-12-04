import sys

from collections import defaultdict

lines = [line for line in sys.stdin.read().splitlines()]


xs = set()
aa = set()
grid = defaultdict(str)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x, y] = c
        if c == "X":
            xs.add((x, y))
        if c == "A":
            aa.add((x, y))


p1 = 0
for x, y in xs:
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue

            for i in range(1, 4):
                nx = x + dx * i
                ny = y + dy * i
                if grid[nx, ny] != "XMAS"[i]:
                    break
            else:
                p1 += 1

print("Part 1:", p1)

p2 = 0
for x, y in aa:
    tl = grid[x - 1, y - 1]
    br = grid[x + 1, y + 1]
    bl = grid[x - 1, y + 1]
    tr = grid[x + 1, y - 1]
    ms = ("M", "S")
    if tl in ms and br in ms and tl != br:
        if bl in ms and tr in ms and bl != tr:
            p2 += 1

print("Part 2:", p2)
