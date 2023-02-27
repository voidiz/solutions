import sys

from collections import defaultdict, deque

lines = sys.stdin.read().splitlines()

neighbors = defaultdict(list)
q1 = deque()
q2 = deque()
e = (0, 0)

for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        curr = line[x]
        if curr == "S" or curr == "a":
            if curr == "S":
                q1.append((0, x, y))

            q2.append((0, x, y))

        if curr == "E":
            e = (x, y)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(line) and 0 <= ny < len(lines):
                n = lines[ny][nx]
                convert = {"S": "a", "E": "z"}
                curr = convert[curr] if curr in convert else curr
                n = convert[n] if n in convert else n
                if ord(n) - ord(curr) <= 1:
                    neighbors[(x, y)].append((nx, ny))


def solve(q: deque) -> int:
    visited = set()
    while q:
        dst, *curr = q.popleft()
        curr = tuple(curr)
        if curr == e:
            return dst

        for n in neighbors[curr]:
            if n not in visited:
                visited.add(n)
                q.append((dst + 1, *n))

    assert False and "unreachable"


print("Part 1:", solve(q1))
print("Part 2:", solve(q2))
