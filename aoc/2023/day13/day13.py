import sys

# fmt: off
sys.path.append("../..")
from lib.list import *
# fmt: on

patterns = sys.stdin.read().split("\n\n")


def check_ref(i, j, lines, fixed=False):
    if i < 0 or j >= len(lines):
        # we must have fixed to complete
        return fixed

    l1 = lines[i]
    l2 = lines[j]

    for c in range(len(l1)):
        if l1[c] == l2[c]:
            continue

        # cant change if fixed earlier
        if fixed:
            return False

        fixed = True

    return check_ref(i - 1, j + 1, lines, fixed)


def solve(part2):
    total = 0
    for pattern in patterns:
        lines = [line for line in pattern.split("\n") if line]
        found = False
        for i in range(len(lines) - 1):
            if check_ref(i, i + 1, lines, not part2):
                total += 100 * (i + 1)
                found = True

        if found:
            continue

        tlines = transpose(lines)
        for i in range(len(tlines) - 1):
            if check_ref(i, i + 1, tlines, not part2):
                total += i + 1
                found = True

        assert found

    return total


print("Part 1:", solve(False))
print("Part 2:", solve(True))
