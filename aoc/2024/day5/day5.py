import sys
import functools

from collections import defaultdict

deps, seqs = sys.stdin.read().split("\n\n")
seqs = [[int(x) for x in seq.split(",")] for seq in seqs.splitlines()]

prev = defaultdict(set)
for dep in deps.splitlines():
    a, b = dep.split("|")
    prev[int(b)].add(int(a))


p1 = 0
for s in seqs:
    for r1, r2 in zip(s, s[1:]):
        if r2 in prev[r1]:
            break
    else:
        p1 += s[len(s) // 2]
print("Part 1:", p1)


def cmp(a, b):
    if b in prev[a]:
        return 1

    return -1


p2 = 0
for s in seqs:
    correct = sorted(s, key=functools.cmp_to_key(cmp))
    if s != correct:
        p2 += correct[len(correct) // 2]
print("Part 2:", p2)
