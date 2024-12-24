import sys
import graphviz

from collections import deque

vals, ns = sys.stdin.read().split("\n\n")
vals = vals.splitlines()
ns = ns.splitlines()

vs = {}
for val in vals:
    init, v = val.split(": ")
    vs[init] = int(v)

dot = graphviz.Digraph()
q = []
for i, n in enumerate(ns):
    left, right = n.split(" -> ")
    lop, op, rop = left.split()
    q.append((lop, op, rop, right))

    gate = f"{i}_{op}"
    dot.node(gate, op, shape="invtriangle")
    if right.startswith("z"):
        dot.node(right, right, fillcolor="green", style="filled")
    dot.edge(lop, gate)
    dot.edge(rop, gate)
    dot.edge(gate, right)


def calc(vs: dict, q: deque):
    while q:
        lop, op, rop, right = q.popleft()

        if lop in vs and rop in vs:
            if op == "XOR":
                vs[right] = vs[lop] ^ vs[rop]
            elif op == "AND":
                vs[right] = vs[lop] & vs[rop]
            elif op == "OR":
                vs[right] = vs[lop] | vs[rop]
        else:
            q.append((lop, op, rop, right))


def get_num(prefix, vs):
    bn = []
    for k, v in vs.items():
        if k.startswith(prefix):
            bn.append((k, v))
    bn.sort(reverse=True)
    return int("".join(str(b[1]) for b in bn), 2)


dot.render(format="pdf")

# valid transitions:
# 1. xor -> (xor, and)
# 2. and -> or
# 3. or -> (xor, and)
# 4. xor -> _ [only for z00-45, must take carry bit if z01-z45]
# 5. or -> _ [carry, can only be bit 46]

# swaps
# hnd, z09
# tdv, z16
# bks, z23
# tjp, nrn

calc(vs, deque(q))
print("Part 1:", get_num("z", vs))
print(
    "Part 2:",
    ",".join(sorted(["hnd", "z09", "tdv", "z16", "bks", "z23", "tjp", "nrn"])),
)
