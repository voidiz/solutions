import sys

from collections import defaultdict

lines = [line for line in sys.stdin.read().splitlines()]

antennas = defaultdict(list)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            antennas[c].append((x, y))

p1 = set()
p2 = set()
for locs in antennas.values():
    for a in locs:
        for b in locs:
            if a == b:
                continue

            dx = a[0] - b[0]
            dy = a[1] - b[1]
            for i in range(9999):
                nx = a[0] + dx * i
                ny = a[1] + dy * i

                if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
                    if i == 1:
                        p1.add((nx, ny))

                    p2.add((nx, ny))
                else:
                    break

print("Part 1:", len(p1))
print("Part 2:", len(p2))
