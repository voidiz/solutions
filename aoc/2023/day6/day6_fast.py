import sys
import re

# fmt: off
sys.path.append("../..")
from lib.search import *
# fmt: on

lines = [line for line in sys.stdin.read().splitlines()]

times = list(map(int, re.findall(r"\d+", lines[0])))
distances = list(map(int, re.findall(r"\d+", lines[1])))

n = len(times)


def count_ways(time, winning):
    def cmp(dst):
        # need at least winning + 1 to beat
        target = winning + 1
        return target - dst

    # distance given elapsed ms of pressing the button
    def dst(elapsed):
        remaining = time - elapsed
        traveled = remaining * elapsed
        return traveled

    # find the time at which we start winning.
    # we want the higher end of the time boundary since we
    # may not find a time that exactly leads to the winning
    # distance + 1
    _, _, high = binary_search(dst, 0, time, cmp)

    remaining = time - high
    return remaining - high + 1


p1 = 1
for i in range(n):
    time = times[i]
    distance = distances[i]
    p1 *= count_ways(time, distance)

print(p1)

time = int("".join(map(str, times)))
distance = int("".join(map(str, distances)))
p2 = count_ways(time, distance)
print(p2)
