import sys
import math

lines = [line for line in sys.stdin.read().splitlines()]
steps = lines[0]

neighbors = {}
for line in lines[2:]:
    current, next = line.split(" = ")

    left, right = next.split(", ")
    left = left[1:]
    right = right[:-1]

    neighbors[current] = (left, right)


def solve(node):
    step = 0
    while node[2] != "Z":
        dir = steps[step % len(steps)]

        if dir == "R":
            node = neighbors[node][1]
        else:
            node = neighbors[node][0]

        step += 1

    return step


p1 = solve("AAA")
print("Part 1:", p1)

p2 = 1
for node in [node for node in neighbors if node[2] == "A"]:
    # this only works because the input has a pattern where
    # if it takes N steps to reach a node, you will reach it
    # again in N steps.

    # then we're just looking for the first step when
    # all of the Ns for the nodes align, i.e., the lcm
    p2 = math.lcm(p2, solve(node))
print("Part 2:", p2)
