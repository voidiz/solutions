import sys

# fmt: off
sys.path.append("../..")
from lib.list import *
# fmt: on

lines = [list(map(int, line)) for line in sys.stdin.read().splitlines()]


def coords(x: int, y: int, rotation: int = 0) -> tuple[int, int]:
    """
    (x, y) in grid rotated by `rotation` -> (x, y) in non-rotated grid
    """
    if rotation == 90:
        return (y, len(lines[0]) - 1 - x)

    if rotation == 180:
        return (len(lines[0]) - 1 - x, len(lines) - 1 - y)

    if rotation == 270:
        return (len(lines) - 1 - y, x)

    return (x, y)


def look(
    grid: list[list[int]], visited: set[tuple[int, int]], rotation: int = 0
) -> None:
    for n, row in enumerate(grid):
        # Add edge
        visited.add(coords(0, n, rotation))

        max_tree = 0
        for i in range(len(row) - 1):
            max_tree = max(max_tree, row[i])
            if max_tree < row[i + 1]:
                visited.add(coords(i + 1, n, rotation))


def score(dir: tuple[int, int], x: int, y: int, curr: int, first: bool = True):
    if not first and (
        x <= 0
        or y <= 0
        or x >= len(lines[0]) - 1
        or y >= len(lines) - 1
        or lines[y][x] >= curr
    ):
        return 0

    dx, dy = dir
    return 1 + score(dir, x + dx, y + dy, curr, False)


visited = set()
for deg in [0, 90, 180, 270]:
    look(rotate(lines, deg), visited, deg)

p2 = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        total = 1
        for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            s = score(dir, x, y, lines[y][x])
            total *= s

        p2 = max(total, p2)


print("Part 1:", len(visited))
print("Part 2:", p2)
