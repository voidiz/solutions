import sys

lines = [line for line in sys.stdin.read().splitlines()]

grid = {}

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x, y] = c


def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue

            yield (x + dx, y + dy)


def solve(grid):
    tot = 0
    new_grid = grid.copy()

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if grid[x, y] == "@":
                papers = 0
                for nx, ny in neighbors(x, y):
                    if (nx, ny) not in grid:
                        continue

                    if grid[nx, ny] == "@":
                        papers += 1

                if papers < 4:
                    new_grid[x, y] = "."
                    tot += 1

    return tot, new_grid


p1 = 0
p2 = 0
while True:
    n, grid = solve(grid)
    if p1 == 0:
        p1 = n

    if n > 0:
        p2 += n
    else:
        break

print("Part 1:", p1)
print("Part 2:", p2)
