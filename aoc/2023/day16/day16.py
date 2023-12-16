import sys

sys.setrecursionlimit(10**6)

lines = [list(line) for line in sys.stdin.read().splitlines()]


def inside(x, y):
    return 0 <= x < len(lines[0]) and 0 <= y < len(lines)


def search(x, y, dx, dy, vis):
    nx = x + dx
    ny = y + dy

    if not inside(nx, ny) or (nx, ny, dx, dy) in vis:
        return

    vis.add((nx, ny, dx, dy))

    c = lines[ny][nx]
    if c == "/":
        if dx == 1:
            dy = -1
            dx = 0
        elif dx == -1:
            dy = 1
            dx = 0
        elif dy == 1:
            dx = -1
            dy = 0
        elif dy == -1:
            dx = 1
            dy = 0

    if c == "\\":
        if dx == 1:
            dx = 0
            dy = 1
        elif dx == -1:
            dx = 0
            dy = -1
        elif dy == 1:
            dx = 1
            dy = 0
        elif dy == -1:
            dx = -1
            dy = 0

    if c == "-":
        if dy in (-1, 1):
            search(nx, ny, -1, 0, vis)
            search(nx, ny, 1, 0, vis)
            return

    if c == "|":
        if dx in (-1, 1):
            search(nx, ny, 0, -1, vis)
            search(nx, ny, 0, 1, vis)
            return

    search(nx, ny, dx, dy, vis)


def solve(x, y, dx, dy):
    vis = set()
    search(x, y, dx, dy, vis)
    return len(set((x, y) for x, y, *_ in vis))


print("Part 1:", solve(-1, 0, 1, 0))

p2 = 0
for y in range(len(lines)):
    p2 = max(p2, solve(-1, y, 1, 0))
    p2 = max(p2, solve(len(lines[0]), y, -1, 0))

for x in range(len(lines[0])):
    p2 = max(p2, solve(x, -1, 0, 1))
    p2 = max(p2, solve(x, len(lines), 0, -1))

print("Part 2:", p2)
