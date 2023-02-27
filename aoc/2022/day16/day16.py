import sys
import functools

from itertools import combinations

lines = [line for line in sys.stdin.read().splitlines()]

neighbors = {}
flows = {}
for line in lines:
    parts = line.split(" ")
    valve = parts[1]
    _, rate = parts[4].split("=")
    flows[valve] = int(rate[:-1])
    neighbors[valve] = [n.rstrip(",") for n in parts[9:]]


@functools.cache
def solve(valve: str, remaining: int, can: frozenset[str]) -> int:
    if remaining <= 0:
        return 0

    best = 0
    for n in neighbors[valve]:
        # try to open the valve
        if valve in can:
            new_can = frozenset(v for v in can if v != valve)
            pressure = flows[valve] * (remaining - 1)
            best = max(best, pressure + solve(n, remaining - 2, new_can))

        # don't open the valve
        best = max(best, solve(n, remaining - 1, can))

    return best


# no need to open valves with flow 0
can_open = set(valve for valve, rate in flows.items() if rate > 0)
print("Part 1:", solve("AA", 30, frozenset(can_open)))

# we only care about subsets that are half the size of can_open
relevant_subsets = list(
    set(c) for c in combinations(can_open, len(can_open) // 2)
)

p2 = 0
for i, subset in enumerate(relevant_subsets):
    c1 = frozenset(subset)
    c2 = frozenset(can_open - subset)

    if i % (max(1, len(relevant_subsets) // 100)) == 0:
        print(f"{i + 1} out of {len(relevant_subsets)} explored")

    a = solve("AA", 26, c1)
    b = solve("AA", 26, c2)
    p2 = max(a + b, p2)

print("Part 2:", p2)
