import sys

from collections import Counter

line = sys.stdin.read().strip().split()


def blink(num):
    if num == 0:
        return [1]

    snum = str(num)
    if len(snum) % 2 == 0:
        left = int(snum[: len(snum) // 2])
        right = int(snum[len(snum) // 2 :])
        return [left, right]

    return [num * 2024]


state = Counter(int(x) for x in line)
for b in range(75):
    if b == 25:
        print("Part 1:", sum(state.values()))

    new_state = Counter()
    for num, amt in state.items():
        for new_num in blink(num):
            new_state[new_num] += amt

    state = new_state

print("Part 2:", sum(state.values()))
