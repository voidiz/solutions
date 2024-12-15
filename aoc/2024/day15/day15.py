import sys

g, dirs = [block.splitlines() for block in sys.stdin.read().split("\n\n")]


g1 = {}
s1 = (-1, -1)
for y, line in enumerate(g):
    for x, c in enumerate(line):
        if c == "@":
            s1 = (x, y)
            g1[x, y] = "."
        else:
            g1[x, y] = c


g2 = {}
s2 = (-1, -1)
for y, line in enumerate(g):
    x = 0
    for c in line:
        if c == "@":
            s2 = (x, y)
            g2[x, y] = "."
            g2[x + 1, y] = "."
        elif c in ("#", "."):
            g2[x, y] = c
            g2[x + 1, y] = c
        elif c == "O":
            g2[x, y] = "["
            g2[x + 1, y] = "]"

        x += 2


def check(x, y, dx, dy, grid):
    nx, ny = x + dx, y + dy

    if grid[nx, ny] == "#":
        return False

    if grid[nx, ny] == ".":
        return True

    if grid[nx, ny] == "O":
        return check(nx, ny, dx, dy, grid)

    d = {"[": 1, "]": -1}[grid[nx, ny]]
    if dx == d:
        return check(nx + d, ny, dx, dy, grid)

    return check(nx, ny, dx, dy, grid) and check(nx + d, ny, dx, dy, grid)


def push(x, y, dx, dy, grid):
    nx, ny = x + dx, y + dy

    if grid[nx, ny] == ".":
        grid[nx, ny], grid[x, y] = grid[x, y], grid[nx, ny]
        return

    if grid[nx, ny] == "O":
        push(nx, ny, dx, dy, grid)
        grid[nx, ny], grid[x, y] = grid[x, y], grid[nx, ny]
        return

    d = {"[": 1, "]": -1}[grid[nx, ny]]
    if dx == d:
        push(nx + d, ny, dx, dy, grid)
        grid[nx + d, ny], grid[nx, ny], grid[x, y] = (
            grid[nx, ny],
            grid[x, y],
            grid[nx + d, ny],
        )
        return

    push(nx, ny, dx, dy, grid)
    push(nx + d, ny, dx, dy, grid)
    grid[nx, ny], grid[x, y] = grid[x, y], grid[nx, ny]


for c in "".join(dirs):
    deltas = {
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
        "^": (0, -1),
    }

    x, y = s1
    dx, dy = deltas[c]
    if check(x, y, dx, dy, g1):
        push(x, y, dx, dy, g1)
        s1 = (x + dx, y + dy)

    x, y = s2
    dx, dy = deltas[c]
    if check(x, y, dx, dy, g2):
        push(x, y, dx, dy, g2)
        s2 = (x + dx, y + dy)

p1 = 0
for (x, y), c in g1.items():
    if c == "O":
        p1 += y * 100 + x
print("Part 1:", p1)

p2 = 0
for (x, y), c in g2.items():
    if c == "[":
        p2 += y * 100 + x
print("Part 2:", p2)
