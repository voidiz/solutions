import sys
import math
import functools
from collections import defaultdict
from heapq import heappush, heappop

Blizzard = defaultdict[tuple[int, int], list[str]]

lines = [line for line in sys.stdin.read().splitlines()]

blizzards: Blizzard = defaultdict(list)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in ["<", ">", "^", "v"]:
            blizzards[(x, y)].append(c)

minx = 0
miny = 0
maxx = len(lines[0]) - 1
maxy = len(lines) - 1

# blizzard pattern repeats every lcm(dimensions) ticks
lcm = math.lcm(maxx - 1, maxy - 1)


def print_blizz(blizz: Blizzard) -> None:
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if x in (minx, maxx) or y in (miny, maxy):
                sys.stdout.write("#")
                continue

            items = blizz[(x, y)]
            if len(items) == 1:
                sys.stdout.write(blizz[(x, y)][0])
            elif len(items) > 0:
                sys.stdout.write(str(len(items)))
            else:
                sys.stdout.write(".")

        sys.stdout.write("\n")

    print()


@functools.cache
def tick(minutes: int) -> Blizzard:
    if minutes == 0:
        return blizzards

    new_blizz = defaultdict(list)
    for (x, y), cs in tick(minutes - 1).items():
        for c in cs:
            nx, ny = x, y
            if c == ">":
                nx += 1
                if nx == maxx:
                    nx = 1
            elif c == "<":
                nx -= 1
                if nx == minx:
                    nx = maxx - 1
            elif c == "^":
                ny -= 1
                if ny == miny:
                    ny = maxy - 1
            elif c == "v":
                ny += 1
                if ny == maxy:
                    ny = 1

            new_blizz[(nx, ny)].append(c)

    return new_blizz


def astar(start: tuple[int, int], end: tuple[int, int], start_minute: int):
    def h(node, minute):
        x1, y1 = node
        x2, y2 = end
        return abs(x2 - x1) + abs(y2 - y1) + minute

    visited = set()

    # heuristic, coords, minute
    q = [(0, start, start_minute)]
    while q:
        curr = heappop(q)
        _, (x, y), minute = curr
        if (x, y) == end:
            return minute

        next_blizz = tick(minute + 1)

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]:
            nx = x + dx
            ny = y + dy
            s = ((nx, ny), (minute + 1) % lcm)
            if (nx, ny) not in (start, end) and (
                nx >= maxx
                or nx <= minx
                or ny >= maxy
                or ny <= miny
                or len(next_blizz[(nx, ny)]) > 0
                or s in visited
            ):
                continue

            visited.add(s)
            heappush(q, ((h((nx, ny), minute + 1), (nx, ny), minute + 1)))

    assert "unreachable" and False


start = (1, 0)
end = (maxx - 1, maxy)
first = astar(start, end, 0)
second = astar(end, start, first)
third = astar(start, end, second)

print("Part 1:", first)
print("Part 2:", third)
