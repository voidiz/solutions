import math
import sys
import re

lines = [line for line in sys.stdin.read().splitlines()]

times = list(map(int, re.findall(r"\d+", lines[0])))
distances = list(map(int, re.findall(r"\d+", lines[1])))

n = len(times)


def count_ways(time, target):
    # formula for the distance d:
    # d = t * (time - t) = -t^2 + time * t
    # <=> t^2 - time * t + d = 0
    # => t = time / 2 - sqrt((time / 2) ** 2 + d) (we want the first t)

    # we want ceil(t), given d = target + 1 (at least 1 more mm than the
    # winning distance).
    t = math.ceil(time / 2 - ((time / 2) ** 2 - (target + 1)) ** 0.5)

    # then, the number of ways is time - 2 * t + 1
    return time - 2 * t + 1


p1 = 1
for i in range(n):
    time = times[i]
    target = distances[i]

    p1 *= count_ways(time, target)

print("Part 1:", p1)

time = int("".join(map(str, times)))
target = int("".join(map(str, distances)))
p2 = count_ways(time, target)
print("Part 2:", p2)
