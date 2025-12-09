import sys

from shapely.geometry import Polygon

lines = [
    tuple(int(x) for x in line.split(","))
    for line in sys.stdin.read().splitlines()
]


def rect(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    xmin, xmax = sorted([x1, x2])
    ymin, ymax = sorted([y1, y2])

    return Polygon([(xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin)])


def area(p):
    xmin, ymin, xmax, ymax = p.bounds
    return (xmax - xmin + 1) * (ymax - ymin + 1)


silver = 0
gold = 0
whole = Polygon(lines)
for i, p1 in enumerate(lines):
    for p2 in lines[i + 1 :]:
        p = rect(p1, p2)
        silver = max(silver, area(p))

        if p.within(whole):
            gold = max(gold, area(p))

print("Part 1:", int(silver))
print("Part 2:", int(gold))
