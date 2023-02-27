import sys
from sympy.solvers import solve
from sympy import Eq, S

lines = sys.stdin.read().splitlines()

eqs = {}
for line in lines:
    lhs, rhs = line.split(": ")
    eqs[lhs] = rhs.split(" ")


def construct(root: str) -> str:
    rhs = eqs[root]
    if len(rhs) == 1:
        return rhs[0]

    return f"({construct(rhs[0])}) {rhs[1]} ({construct(rhs[2])})"


print("Part 1:", solve(Eq(S("x"), S(construct(("root")))))[0])

eqs["humn"] = "x"
lhs, rhs = eqs["root"][0], eqs["root"][2]
del eqs["root"]
print("Part 2:", solve(Eq(S(construct(lhs)), S(construct(rhs))))[0])
