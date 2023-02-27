import sys
import functools

pairs = [pair.strip() for pair in sys.stdin.read().split("\n\n")]


def cmp(left: list, right: list) -> int:
    leftint = isinstance(left, int)
    rightint = isinstance(right, int)
    leftlst = isinstance(left, list)
    rightlst = isinstance(right, list)

    if leftint and rightint:
        if left < right:
            return -1
        if left == right:
            return 0
        if left > right:
            return 1

    if leftlst and rightlst:
        if len(left) == len(right) == 0:
            return 0

        if len(left) == 0:
            return -1

        if len(right) == 0:
            return 1

        # really? why not compare the whole list :(
        res = cmp(left[0], right[0])
        if res in [1, -1]:
            return res

        return cmp(left[1:], right[1:])

    if leftint and rightlst:
        return cmp([left], right)

    if leftlst and rightint:
        return cmp(left, [right])

    assert False and "unreachable"


p1 = 0
packets = [[[2]], [[6]]]
for i, pair in enumerate(pairs):
    a, b = map(eval, pair.split("\n"))
    packets += [a, b]

    if cmp(a, b) == -1:
        p1 += i + 1

packets.sort(key=functools.cmp_to_key(cmp))

print("Part 1:", p1)
print("Part 2:", (1 + packets.index([[2]])) * (1 + packets.index([[6]])))
