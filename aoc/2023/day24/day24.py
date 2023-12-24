import sys
import re
import itertools

from z3 import Solver, Int

lines = [line for line in sys.stdin.read().splitlines()]
rocks = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]
lower = 200000000000000
upper = 400000000000000


def line_intersection(l1, l2):
    x11, y11, x12, y12 = l1
    x21, y21, x22, y22 = l2

    # k = dy/dx
    k1 = (y12 - y11) / (x12 - x11)
    k2 = (y22 - y21) / (x22 - x21)

    if k1 == k2:
        return None

    # m = y - kx
    m1 = y11 - k1 * x11
    m2 = y21 - k2 * x21

    # k1x + m1 = k2x + m2
    x = (m2 - m1) / (k1 - k2)

    # y = kx + m
    y = k1 * x + m1

    return x, y


p1 = 0
for r1, r2 in itertools.combinations(rocks, 2):
    x1, y1, _, dx1, dy1, _ = r1
    x2, y2, _, dx2, dy2, _ = r2

    l1 = (x1, y1, x1 + dx1, y1 + dy1)
    l2 = (x2, y2, x2 + dx2, y2 + dy2)

    intersection = line_intersection(l1, l2)
    if intersection:
        x, y = intersection

        dir1 = (dx1 > 0 and x > x1) or (dx1 < 0 and x < x1)
        dir2 = (dx2 > 0 and x > x2) or (dx2 < 0 and x < x2)

        if dir1 and dir2 and lower <= x <= upper and lower <= y <= upper:
            p1 += 1


print("Part 1:", p1)

vars = [Int(var) for var in ["x", "y", "z", "dx", "dy", "dz"]]

s = Solver()
for i in range(len(rocks)):
    rock = rocks[i]
    t = Int(f"t{i}")

    for dim in range(3):
        s.add(vars[dim] + vars[dim + 3] * t == rock[dim] + rock[dim + 3] * t)

s.check()
print("Part 2:", s.model().eval(sum(vars[:3])))
