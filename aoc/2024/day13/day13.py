import re
import sys

games = sys.stdin.read().split("\n\n")


def solve(ax, ay, bx, by, px, py):
    # ax * a + bx * b = px
    # ay * a + by * b = py
    det = ax * by - ay * bx
    a = (by * px - bx * py) / det
    b = (-ay * px + ax * py) / det
    return a, b


p1 = 0
p2 = 0
for game in games:
    ax, ay, bx, by, px, py = [int(v) for v in re.findall(r"\d+", game)]

    for b in [0, 10**13]:
        res = solve(ax, ay, bx, by, px + b, py + b)
        if all(v.is_integer() for v in res):
            if b == 0:
                p1 += res[0] * 3 + res[1]
            else:
                p2 += res[0] * 3 + res[1]

print("Part 1:", int(p1))
print("Part 2:", int(p2))
