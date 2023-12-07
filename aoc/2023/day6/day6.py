import sys
import re

lines = [line for line in sys.stdin.read().splitlines()]

times = list(map(int, re.findall(r"\d+", lines[0])))
distances = list(map(int, re.findall(r"\d+", lines[1])))

n = len(times)

p1 = 1
for i in range(n):
    time = times[i]
    distance = distances[i]

    for t in range(time + 1):
        speed = t
        remaining_time = time - t
        can_travel = remaining_time * speed
        if can_travel > distance:
            p1 *= remaining_time - t + 1
            break

print("Part 1:", p1)

time = int("".join([str(time) for time in times]))
distance = int("".join([str(dist) for dist in distances]))

p2 = 0
for t in range(time + 1):
    speed = t
    remaining_time = time - t
    can_travel = remaining_time * speed
    if can_travel > distance:
        p2 += remaining_time - t + 1
        break

print("Part 2:", p2)
