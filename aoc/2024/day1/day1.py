import sys

from collections import Counter

lines = sys.stdin.read().splitlines()

left = []
right = []
for line in lines:
    s = list(map(int, line.split()))
    left += [s[0]]
    right += [s[1]]

left.sort()
right.sort()

ct = Counter(right)

p1 = 0
p2 = 0
for i in range(len(left)):
    p1 += abs(left[i] - right[i])
    p2 += left[i] * ct[left[i]]

print("Part 1:", p1)
print("Part 2:", p2)
