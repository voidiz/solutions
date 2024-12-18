import sys

from heapq import heappop, heappush
from collections import defaultdict

lines = [line for line in sys.stdin.read().splitlines()]


def run(bs):
    grid = {}
    for n, line in enumerate(lines):
        if n < bs:
            x, y = line.split(",")
            grid[int(x), int(y)] = "#"

    end = (70, 70)
    # end = (6, 6)

    h = []
    heappush(h, (0, 0, 0))
    dists = defaultdict(lambda: 10**10)
    dists[0, 0] = 0

    while h:
        d, x, y = heappop(h)

        if (x, y) == end:
            return False, d

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = dx + x
            ny = dy + y

            if not (0 <= nx <= end[0] and 0 <= ny <= end[1]):
                continue

            if (nx, ny) in grid and grid[nx, ny] == "#":
                continue

            ndst = d + 1
            if ndst < dists[nx, ny]:
                dists[nx, ny] = ndst
                heappush(h, (ndst, nx, ny))

    return True, -1


print("Part 1:", run(1024)[1])
for n in range(1024, 100000):
    if run(n)[0]:
        print("Part 2:", lines[n - 1])
        break
