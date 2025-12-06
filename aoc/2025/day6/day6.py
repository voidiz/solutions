import sys

# fmt: off
sys.path.append("../..")
from lib.list import *
# fmt: on

lines = [line for line in sys.stdin.read().splitlines()]


def silver():
    ops = [item.strip() for item in lines[-1].split()]

    p1 = 0
    lists = [[] for _ in range(len(lines[0].split()))]
    for line in lines[:-1]:
        for i, num in enumerate(line.split()):
            lists[i].append(int(num.strip()))

    p1 = 0
    for i, ls in enumerate(lists):
        op = ops[i]
        p1 += eval(op.join((str(x) for x in ls)))

    return p1


def gold(lines):
    lines = transpose(lines)

    p2 = 0
    curr = 0
    op = ""

    for line in lines:
        line = [c for c in line if c != " "]
        if "*" in line or "+" in line:
            p2 += curr
            op = line[-1]
            curr = int("".join(line[0:-1]))
            continue

        if not line:
            continue

        num = "".join(line)
        curr = eval("".join(map(str, (curr, op, num))))

    p2 += curr

    return p2


print("Part 1:", silver())
print("Part 2:", gold(lines))
