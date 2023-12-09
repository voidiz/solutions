import sys

lines = [line for line in sys.stdin.read().splitlines()]
histories = [list(map(int, line.split())) for line in lines]


def calc(history):
    if all(val == 0 for val in history):
        return 0

    next_step = [b - a for a, b in zip(history, history[1:])]
    return calc(next_step) + history[-1]


print("Part 1:", sum(map(calc, histories)))
print("Part 2:", sum(map(calc, [history[::-1] for history in histories])))
