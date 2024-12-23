import sys
import networkx as nx

lines = [line for line in sys.stdin.read().splitlines()]

G = nx.Graph()
for line in lines:
    a, b = line.split("-")
    G.add_edge(a, b)


cs = list(nx.enumerate_all_cliques(G))
p1 = 0
for c in cs:
    if len(c) == 3 and any(n.startswith("t") for n in c):
        p1 += 1

print("Part 1:", p1)
print("Part 2:", ",".join(sorted(cs[-1])))
