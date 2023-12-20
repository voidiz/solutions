import sys
import math

from collections import defaultdict
from dataclasses import dataclass

lines = [line for line in sys.stdin.read().splitlines()]


@dataclass
class Module:
    name: str
    prefix: str  # % or &
    is_on: bool
    last_received_from: dict  # parent -> low/high


modules = {}
neighbors = defaultdict(list)
parents = defaultdict(list)
for line in lines:
    module, ns = line.split(" -> ")

    if "%" in module:
        name = module[1:]
        m = Module(name, module[0], False, {})
    elif "&" in module:
        name = module[1:]
        m = Module(name, module[0], True, {})
    else:
        # broadcaster
        name = module
        m = Module(name, module[0], True, {})

    modules[name] = m
    for n in ns.split(", "):
        parents[n].append(name)
        neighbors[name].append(n)

for m in modules.values():
    if m.prefix == "&":
        for p in parents[m.name]:
            m.last_received_from[p] = "low"


first = ("broadcaster", "low", "button")
los = 0
his = 0

# part 2, need a low pulse sent to rx
# for my input:
#   rx only takes input from df which is a conjunction module.
#   df takes input from &gp, &xp, &ln, &xl (also conjunction modules).
#   all of these need to send high to df for df to send a low pulse to rx.
#   assuming that this happens for each one periodically, independently
#   from the other three, (because that seems to be the pattern this year),
#   the answer is the lcm of these periods.
rx_parent = parents["rx"][0]
deps = parents[rx_parent]
periods = {}

for i in range(1, 10**10):
    los += 1
    q = []
    q.append(first)
    while q:
        name, pulse, prev = q.pop(0)

        if prev in deps and not prev in periods and pulse == "high":
            periods[prev] = i

        if name not in modules:
            continue

        m = modules[name]

        npulse = pulse

        if m.prefix == "%":
            if pulse == "high":
                continue

            m.is_on = not m.is_on

            if m.is_on:
                npulse = "high"
            else:
                npulse = "low"
        elif m.prefix == "&":
            m.last_received_from[prev] = pulse

            if all(v == "high" for v in m.last_received_from.values()):
                npulse = "low"
            else:
                npulse = "high"

        for n in neighbors[name]:
            if npulse == "low":
                nn = (n, npulse, name)
                los += 1
            else:
                nn = (n, npulse, name)
                his += 1

            q.append(nn)

    if i == 1000:
        print("Part 1:", los * his)

    if len(periods) == len(deps):
        print("Part 2:", math.lcm(*periods.values()))

    if len(periods) == len(deps) and i >= 1000:
        break
