import sys

from collections import deque

lines = [line for line in sys.stdin.read().splitlines()]

grid = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x, y] = int(c)


def bfs(x, y, p2):
    q = deque([(x, y)])

    tot = 0
    visited = set()
    while q:
        x, y = q.popleft()
        d = grid[x, y]

        if d == 9:
            tot += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy

            if (nx, ny) not in grid:
                continue

            if not p2 and (nx, ny) in visited:
                continue

            if grid[nx, ny] == d + 1:
                q.append((nx, ny))
                visited.add((nx, ny))

    return tot


p1 = 0
p2 = 0
for (x, y), c in grid.items():
    if c == 0:
        p1 += bfs(x, y, False)
        p2 += bfs(x, y, True)

print("Part 1:", p1)
print("Part 2:", p2)
