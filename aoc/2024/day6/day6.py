import sys

lines = sys.stdin.read().splitlines()

start = (-1, -1)
grid = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "^":
            start = (x, y)
            grid[(x, y)] = "."
        else:
            grid[(x, y)] = c


def run(x, y, visited, dir):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    while True:
        if (x, y, dir) in visited:
            return True

        visited.add((x, y, dir))

        dx, dy = dirs[dir]
        nx = x + dx
        ny = y + dy
        if (nx, ny) not in grid:
            return False

        if grid[nx, ny] == "#":
            dir = (dir + 1) % 4
            continue

        x, y = nx, ny


visited = set()
run(*start, visited, 0)
visited_coords = set((x, y) for x, y, _ in visited)
print("Part 1:", len(visited_coords))

p2 = 0
for bx, by in visited_coords:
    grid[bx, by] = "#"
    if run(*start, set(), 0):
        p2 += 1

    grid[bx, by] = "."

print("Part 2:", p2)
