import sys
import functools

from collections import defaultdict

lines = [line for line in sys.stdin.read().splitlines()]

ns = defaultdict(list)

for line in lines:
    start, n = line.split(": ")
    n = n.split(" ")

    ns[start] += n


@functools.cache
def traverse(node, fft, dac, p1):
    if node == "out":
        return int((fft and dac) or p1)

    fft = fft or node == "fft"
    dac = dac or node == "dac"

    tot = 0
    for n in ns[node]:
        tot += traverse(n, fft, dac, p1)

    return tot


print("Part 1:", traverse("you", False, False, True))
print("Part 2:", traverse("svr", False, False, False))
