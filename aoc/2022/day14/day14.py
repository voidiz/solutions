import sys

from collections import defaultdict

lines = [line for line in sys.stdin.read().splitlines()]
cave = defaultdict(lambda: ".")
maxy = 0

for path in lines:
    rocks = path.split(" -> ")
    for i in range(len(rocks) - 1):
        px, py = map(int, rocks[i].split(","))
        cx, cy = map(int, rocks[i + 1].split(","))
        maxy = max(maxy, py, cy)

        for y in range(abs(cy - py) + 1):
            ny = min(cy, py)
            cave[(cx, ny + y)] = "#"

        for x in range(abs(cx - px) + 1):
            nx = min(cx, px)
            cave[(nx + x, cy)] = "#"

sand = (500, 0)
total = 0
p1 = 0
p1_done = False
while "poggers":
    x, y = sand
    nx, ny = x, y + 1

    if ny > maxy and not p1_done:
        p1 = total
        p1_done = True

    if ny < maxy + 2:
        if cave[(nx, ny)] not in ("#", "o"):
            sand = (nx, ny)
            continue

        if cave[(nx - 1, ny)] not in ("#", "o"):
            sand = (nx - 1, ny)
            continue

        if cave[(nx + 1, ny)] not in ("#", "o"):
            sand = (nx + 1, ny)
            continue

    total += 1
    cave[sand] = "o"
    if sand == (500, 0):
        break

    sand = (500, 0)


print("Part 1:", p1)
print("Part 2:", total)
