import sys
from collections import deque

lines = [line for line in sys.stdin.read().splitlines()]


def solve(sz):
    q = deque()
    for n, l in enumerate(lines[0]):
        if len(q) == sz:
            if len(set(q)) == sz:
                return n

            q.popleft()

        q.append(l)


print("Part 1:", solve(4))
print("Part 2:", solve(14))
