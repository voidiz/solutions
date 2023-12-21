import sys

from collections import deque
from numpy.polynomial import Polynomial as P

lines = [list(line) for line in sys.stdin.read().splitlines()]

S = (0, 0)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            S = (x, y)


def count_pts(visited, odd):
    total = 0
    for x, y in visited:
        if (abs(x - S[0]) + abs(y - S[1])) % 2 == int(odd):
            total += 1
    return total


q = deque()
q.append((0, *S))
visited = set()
visited.add(S)

p1 = 1
ps = {}

while q:
    d, x, y = q.popleft()

    if d == 64:
        p1 = count_pts(visited, False)

    # amount of points when we've reached S again and the pattern repeats
    if d % len(lines) == S[1]:
        if not d in ps:
            # the grid has odd size, so we need to alternate between
            # counting even and odd points
            ps[d] = count_pts(visited, len(ps) % 2 == 0)
            if len(ps) == 3:
                break

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        lx = nx % len(lines[0])
        ly = ny % len(lines)

        if lines[ly][lx] != "#" and (nx, ny) not in visited:
            q.append((d + 1, nx, ny))
            visited.add((nx, ny))


# fit a (quadratic) polynomial to the points
f = P.fit(list(ps.keys()), list(ps.values()), 2)

print("Part 1:", p1)
print("Part 2:", f(26501365))
