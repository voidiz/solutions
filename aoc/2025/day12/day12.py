import sys

*_, layouts = sys.stdin.read().split("\n\n")

p1 = 0
for line in layouts.splitlines():
    sz, amts = line.strip().split(": ")
    w, h = map(int, sz.split("x"))

    req = sum(int(x) for x in amts.split(" "))
    if req <= (w // 3) * (h // 3):
        p1 += 1

print("Part 1:", p1)
