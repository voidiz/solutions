import sys
import itertools

from collections import Counter

# fmt: off
sys.path.append("../..")
from lib.list import *
# fmt: on

grids = [grid.splitlines() for grid in sys.stdin.read().split("\n\n")]

p1 = 0
for g1, g2 in itertools.combinations(grids, 2):
    if g1[0] == g2[0]:
        continue

    r1 = rotate90(g1)
    r2 = rotate90(g2)
    for i in range(len(r1)):
        if not Counter(r1[i])["#"] + Counter(r2[i])["#"] <= 7:
            break
    else:
        p1 += 1

print("Part 1:", p1)
