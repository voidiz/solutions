import sys
from collections import defaultdict

lines = [line for line in sys.stdin.read().splitlines()]

sizes = defaultdict(int)
cwd = []

for line in lines:
    args = line.split(" ")
    if line.startswith("$ cd"):
        cmd = args[1]
        path = args[2]
        if path == "..":
            cwd.pop()
            continue

        if path == "/":
            cwd = ["/"]
            continue

        cwd.append(path)

    if args[0].isnumeric():
        for i in range(len(cwd)):
            sizes["/".join(cwd[: i + 1])] += int(args[0])


free_space = 70000000 - sizes["/"]
target = 30000000
target_diff = abs(free_space - target)

p1 = sum(sz for sz in sizes.values() if sz <= 100000)
p2 = min(sizes.values(), key=lambda sz: abs(sz - target_diff))

print("Part 1:", p1)
print("Part 2:", p2)
