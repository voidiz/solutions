import sys
import functools

patterns, designs = sys.stdin.read().split("\n\n")
patterns = patterns.split(", ")
designs = designs.splitlines()


@functools.cache
def match(rem: str):
    if rem == "":
        return 1

    tot = 0
    for pat in patterns:
        if rem.startswith(pat):
            tot += match(rem[len(pat) :])

    return tot


p1 = 0
p2 = 0
for d in designs:
    res = match(d)
    if res > 0:
        p1 += 1

    p2 += res

print("Part 1:", p1)
print("Part 2:", p2)
