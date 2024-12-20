import sys

from collections import Counter

lines = [line for line in sys.stdin.read().splitlines()]

grid = {}
start = (0, 0)
end = (0, 0)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            grid[x, y] = "."
            start = (x, y)
        elif c == "E":
            grid[x, y] = "."
            end = (x, y)
        else:
            grid[x, y] = c


def dfs(x, y, visited):
    if (x, y) == end:
        return [end]

    visited.add((x, y))

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if (nx, ny) in visited:
            continue

        if (nx, ny) not in grid:
            continue

        if grid[nx, ny] == ".":
            res = dfs(nx, ny, visited)
            if res:
                return [(x, y)] + res

    return []


sys.setrecursionlimit(10**8)
p = dfs(*start, set())

s1 = Counter()
s2 = Counter()
for n1 in range(len(p)):
    x1, y1 = p[n1]
    for n2 in range(n1 + 3, len(p)):
        x2, y2 = p[n2]
        dst = abs(x1 - x2) + abs(y1 - y2)
        saved = n2 - n1 - dst
        if dst == 2 and saved >= 100:
            s1[saved] += 1

        if dst <= 20 and saved >= 100:
            s2[saved] += 1

print("Part 1:", sum(v for v in s1.values()))
print("Part 2:", sum(v for v in s2.values()))
