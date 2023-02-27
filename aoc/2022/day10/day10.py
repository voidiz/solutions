import sys

# fmt: off
sys.path.append("../..")
from lib.list import *
# fmt: on

lines = [line for line in sys.stdin.read().splitlines()]


def printcrt(crt: list[list[str]]) -> None:
    print("\n".join("".join(line) for line in crt))


p1 = 0
X = 1
cycle = 1
n = 0
instr = (0, 0)
crt = [["." for _ in range(40)] for _ in range(6)]

while n < len(lines):
    line = lines[n]
    val, time = instr

    if time == 0:
        n += 1
        X += val

        if line != "noop":
            _, new_val = line.split(" ")
            instr = (int(new_val), 1)
        else:
            instr = (0, 0)
    else:
        instr = (val, time - 1)

    if cycle in [20, 60, 100, 140, 180, 220]:
        p1 += cycle * X

    crtx = (cycle - 1) % 40
    crty = (cycle - 1) // 40
    if crtx in [X - 1, X, X + 1]:
        crt[crty][crtx] = "#"

    cycle += 1


print("Part 1:", p1)
print("Part 2:")
printcrt(crt)
