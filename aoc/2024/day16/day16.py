import sys

from heapq import heappop, heappush
from collections import defaultdict

lines = sys.stdin.read().splitlines()

start = (0, 0)
end = (0, 0)
grid = defaultdict(lambda: "x")

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            start = x, y
            grid[x, y] = "."
        elif c == "E":
            end = x, y
            grid[x, y] = "."
        else:
            grid[x, y] = c

h = []
heappush(h, (0, *start, 0, [start]))
dists = defaultdict(lambda: 10**10)
dists[start[0], start[1], 0] = 0
vis = set()
fd = -1

while h:
    d, x, y, dt, p = heappop(h)

    if (x, y) == end:
        fd = d
        vis.update(p)

    if fd != -1:
        continue

    dts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for ndt in (dt, (dt + 1) % 4, (dt - 1) % 4):
        ndx, ndy = dts[ndt]
        nx = x + ndx
        ny = y + ndy
        nd = d + 1 if dt == ndt else d + 1001
        if grid[nx, ny] == "." and nd <= dists[nx, ny, ndt]:
            np = p + [(nx, ny)]
            heappush(h, (nd, nx, ny, ndt, np))
            dists[nx, ny, ndt] = nd

print("Part 1:", fd)
print("Part 2:", len(vis))
