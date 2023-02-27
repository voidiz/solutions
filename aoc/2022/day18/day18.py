import sys
import functools

from collections import deque

lines = [line for line in sys.stdin.read().splitlines()]
covered = set()
nodes = []
for line in lines:
    x, y, z = map(int, line.split(","))
    covered.add((x, y, z))
    nodes.append((x, y, z))

(minx, maxx), (miny, maxy), (minz, maxz) = [
    (min(comp), max(comp)) for comp in zip(*nodes)
]


def neighbors(node):
    sides = [
        [1, 0, 0],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1],
    ]

    x, y, z = node
    for dx, dy, dz in sides:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) not in covered:
            yield nx, ny, nz


@functools.cache
def bfs(node):
    visited = set()
    visited.add(node)

    q = deque([node])
    while q:
        top = q.popleft()
        x, y, z = top

        if not all((minx <= x <= maxx, miny <= y <= maxy, minz <= z <= maxz)):
            return True

        for n in neighbors(top):
            if n in visited:
                continue

            q.append(n)
            visited.add(n)

    return False


p1 = 0
p2 = 0
for node in nodes:
    for n in neighbors(node):
        if n not in covered:
            p1 += 1

        if bfs(n):
            p2 += 1

print("Part 1:", p1)
print("Part 2:", p2)
