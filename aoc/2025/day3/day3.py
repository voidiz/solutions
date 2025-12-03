import sys
import functools


lines = [line for line in sys.stdin.read().splitlines()]


p1 = 0
p2 = 0

for line in lines:

    @functools.cache
    def solve(s, k):
        if not s:
            if k == 0:
                return ""

            return None

        rest = solve(s[1:], k - 1)
        best = solve(s[1:], k)

        if rest is not None:
            r = s[0] + rest
            if best is None or int(r) > int(best):
                best = r

        return best

    pp1 = solve(line, 2)
    assert pp1

    pp2 = solve(line, 12)
    assert pp2

    p1 += int(pp1)
    p2 += int(pp2)

print("Part 1:", p1)
print("Part 2:", p2)
