import sys
import functools

from collections import deque

lines = [list(line) for line in sys.stdin.read().splitlines()]

S = (1, 0)
E = (len(lines[0]) - 2, len(lines) - 1)


def neighbors(x, y, part2):
    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if not part2:
        match lines[y][x]:
            case ">":
                adj = [(1, 0)]
            case "v":
                adj = [(0, 1)]

    for dx, dy in adj:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
            if lines[ny][nx] != "#":
                yield nx, ny


@functools.cache
def find_adj_intersections(start, part2):
    q = deque()
    vis = set()

    q.append((*start, 0))
    vis.add(start)

    adj = []
    while q:
        x, y, d = q.popleft()
        ns = list(neighbors(x, y, part2))

        if len(ns) > 2 and (x, y) != start or (x, y) == E:
            # this is an intersection
            adj.append((x, y, d))
            continue

        for n in ns:
            if not n in vis:
                q.append((*n, d + 1))
                vis.add(n)

    return adj


def dfs(x, y, visited, part2):
    if (x, y) == E:
        return 0

    best = -(10**9)
    for nx, ny, d in find_adj_intersections((x, y), part2):
        if not (nx, ny) in visited:
            best = max(best, d + dfs(nx, ny, visited | {(nx, ny)}, part2))

    return best


print("Part 1:", dfs(*S, set(), False))
print("Part 2:", dfs(*S, set(), True))
