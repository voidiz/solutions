import sys
import networkx as nx

lines = [line for line in sys.stdin.read().splitlines()]

G = nx.Graph()

for line in lines:
    a, bs = line.split(": ")
    for b in bs.split():
        G.add_edge(a, b, capacity=1)

# any global cut of size 3
for s in G.nodes():
    for t in G.nodes():
        if s == t:
            continue

        sz, (a, b) = nx.minimum_cut(G, s, t)
        if sz == 3:
            print("Part 1:", len(a) * len(b))
            exit(0)
