import sys

lines = [line for line in sys.stdin.read().splitlines()]


def deter(x1, x2, y1, y2):
    return x1 * y2 - x2 * y1


x1 = y1 = x2 = y2 = p1 = p2 = points1 = points2 = 0
for line in lines:
    d1, l1, c = line.split()
    l1 = int(l1)

    c = c[2:-1]
    d2 = "RDLU"[int(c[-1])]
    l2 = int(c[:-1], 16)

    dirs = {"R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1)}

    dx1, dy1 = dirs[d1]
    dx2, dy2 = dirs[d2]

    # shoelace formula
    nx1 = x1 + dx1 * l1
    ny1 = y1 + dy1 * l1

    nx2 = x2 + dx2 * l2
    ny2 = y2 + dy2 * l2

    p1 += deter(x1, nx1, y1, ny1)
    p2 += deter(x2, nx2, y2, ny2)

    # points used for exterior area
    points1 += l1
    points2 += l2

    x1 = nx1
    x2 = nx2
    y1 = ny1
    y2 = ny2

# pick's theorem
print("Part 1:", p1 // 2 + points1 // 2 + 1)
print("Part 2:", p2 // 2 + points2 // 2 + 1)
