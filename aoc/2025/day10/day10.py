import sys
import z3

from collections import deque


lines = [line for line in sys.stdin.read().splitlines()]


def solve_p1(states, buttons):
    masks = []
    for button in buttons:
        mask = 0
        for i in button:
            mask |= 1 << i

        masks.append(mask)

    target = 0
    for i, s in enumerate(states):
        if s:
            target |= 1 << i

    q = deque([(0, 0)])
    seen = set([0])

    while q:
        s, changes = q.popleft()
        for mask in masks:
            ns = s ^ mask
            if ns == target:
                return changes + 1

            if ns not in seen:
                q.append((ns, changes + 1))
                seen.add((ns))

    assert False


def solve_p2(lights, buttons):
    # Ax = B
    # A[i][j] = 1 if i:th light affected by j:th button
    # x[j] = how many times the j:th button is pressed
    # B[i] = joltage of i:th light
    # minimize x

    A = [[0] * len(buttons) for _ in range(len(lights))]
    for j, btn in enumerate(buttons):
        for idx in btn:
            A[idx][j] += 1

    x = [z3.Int(f"x_{j}") for j in range(len(buttons))]

    opt = z3.Optimize()
    for j in range(len(buttons)):
        opt.add(x[j] >= 0)

    for i in range(len(lights)):
        opt.add(
            z3.Sum(A[i][j] * x[j] for j in range(len(buttons))) == lights[i]
        )

    opt.minimize(z3.Sum(x))
    assert opt.check() == z3.sat

    model = opt.model()

    return sum(model[x[j]].as_long() for j in range(len(buttons)))


p1 = 0
p2 = 0

for line in lines:
    items = line.split(" ")
    states = [1 if c == "#" else 0 for c in items[0][1:-1]]
    buttons = [
        list(map(int, button[1:-1].split(","))) for button in items[1:-1]
    ]
    targets = list(map(int, items[-1][1:-1].split(",")))

    p1 += solve_p1(states, buttons)

    p2_res = solve_p2(targets, buttons)
    assert p2_res is not None

    p2 += p2_res

print("Part 1:", p1)
print("Part 2:", p2)
