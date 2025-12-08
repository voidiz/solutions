import sys
import math

import networkx as nx

lines = [
    tuple(map(int, line.split(","))) for line in sys.stdin.read().splitlines()
]


def silver(lines):
    n = len(lines)
    G = nx.Graph()
    G.add_nodes_from(range(n))

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((math.dist(lines[i], lines[j]), i, j))

    edges.sort(key=lambda x: x[0])
    for _, u, v in edges[:n]:
        G.add_edge(u, v)

    ccs = [len(c) for c in nx.connected_components(G)]
    ccs.sort(reverse=True)

    return ccs[0] * ccs[1] * ccs[2]


def gold(lines):
    n = len(lines)
    G = nx.Graph()
    G.add_nodes_from(range(n))

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.dist(lines[i], lines[j])
            edges.append((dist, i, j))

    edges.sort(key=lambda x: x[0])
    for _, u, v in edges:
        G.add_edge(u, v)
        if nx.is_connected(G):
            return lines[u][0] * lines[v][0]


print("Part 1:", silver(lines))
print("Part 2:", gold(lines))
