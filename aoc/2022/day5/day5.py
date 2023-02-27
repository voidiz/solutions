import sys
import re

from copy import deepcopy


parts = sys.stdin.read().split("\n\n")
lines = parts[0].split("\n")
width = int(re.findall(r"\d+", lines[-1])[-1])
cols1 = [[] for _ in range(width)]

for i in range(width):
    for line in lines[:-1]:
        col = i + 1
        amt = line[i * 4 + 1]
        if not amt.isspace():
            cols1[i].append(amt)

cols1 = [col[::-1] for col in cols1]
cols2 = deepcopy(cols1)

for inst in parts[1].splitlines():
    amt, frm, to = map(int, re.findall(r"\d+", inst))
    frm -= 1
    to -= 1

    cols1[to] += cols1[frm][-amt:][::-1]
    del cols1[frm][-amt:]

    cols2[to] += cols2[frm][-amt:]
    del cols2[frm][-amt:]

part1 = "".join([cols1[i][-1] for i in range(width)])
part2 = "".join([cols2[i][-1] for i in range(width)])

print("Part 1:", part1)
print("Part 2:", part2)
