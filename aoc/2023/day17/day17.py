import sys

from heapq import heappop, heappush

lines = [
    list([int(c) for c in line]) for line in sys.stdin.read().splitlines()
]


def inside(x, y):
    return 0 <= x < len(lines[0]) and 0 <= y < len(lines)


def get_neighbors(x, y, dir, t, mint=1, maxt=3):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        # can't go in reverse
        if (dx, dy) == (dir[0] * -1, dir[1] * -1):
            continue

        if (dx, dy) == dir:
            if t < maxt and inside(x + dx, y + dy):
                neighbors.append((x + dx, y + dy, dir, t + 1))
        else:
            xx = x + dx * mint
            yy = y + dy * mint
            if inside(xx, yy):
                neighbors.append((xx, yy, (dx, dy), mint))

    return neighbors


def dist(x, y, nx, ny):
    xmin = min(x, nx)
    xmax = max(x, nx)
    ymin = min(y, ny)
    ymax = max(y, ny)

    return sum(
        lines[r][c]
        for r in range(ymin, ymax + 1)
        for c in range(xmin, xmax + 1)
        if not (x == c and y == r)
    )


goal = (len(lines[0]) - 1, len(lines) - 1)


def solve(part2):
    mint = 4 if part2 else 1
    maxt = 10 if part2 else 3

    # d, x, y, dir, t
    q = []
    q.append((0, 0, 0, (0, 0), 0))

    vis = set()

    while q:
        current = heappop(q)
        d, x, y, dir, t = current

        if (x, y, dir, t) in vis:
            continue

        vis.add((x, y, dir, t))

        if (x, y) == goal:
            return d

        for nx, ny, ndir, nt in get_neighbors(x, y, dir, t, mint, maxt):
            nd = d + dist(x, y, nx, ny)
            heappush(q, (nd, nx, ny, ndir, nt))


print("Part 1:", solve(False))
print("Part 2:", solve(True))
