import sys
import re

lines = [line for line in sys.stdin.read().splitlines()]

sensors = {}

for line in lines:
    x1, y1, x2, y2 = map(int, re.findall(r"-?\d+", line))
    dist = abs(y1 - y2) + abs(x1 - x2)
    sensors[(x1, y1)] = dist


p1 = set()
# size = 20 + 1
size = 4_000_000 + 1
row_intervals = [[] for _ in range(size)]

for row in range(size):
    for sensor, dist in sensors.items():
        x, y = sensor

        if y + dist < row or y - dist > row:
            # don't care about sensors that are too far away
            continue

        ydiff = abs(y - row)
        xdiff = dist - ydiff
        interval = (x - xdiff, x + xdiff)

        # mark interval as beacon cannot exist
        row_intervals[row].append(interval)

        # part 1
        if row == 2_000_000:
            for i in range(x - xdiff, x + xdiff):
                if (i, row) != sensor:
                    p1.add((i, row))

final_intervals = [[] for _ in range(size)]
for n, row in enumerate(row_intervals):
    row.sort()
    i = 1
    prev = row[0]
    while i < len(row):
        pa, pb = prev
        ca, cb = row[i]

        # combine intervals overlapping or next to each other
        if ca > pb + 1:
            final_intervals[n].append(prev)
            prev = (ca, cb)
            i += 1
            continue

        prev = (min(pa, ca), max(pb, cb))
        i += 1

    final_intervals[n].append(prev)


print("Part 1:", len(p1))
for y, intervals in enumerate(final_intervals):
    # find the only row split into two intervals
    if len(intervals) == 2:
        x = intervals[0][1] + 1
        print("Part 2:", x * 4_000_000 + y)
        break
