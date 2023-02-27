import sys

from copy import deepcopy

winds = [1 if inst == ">" else -1 for inst in sys.stdin.read().strip()]

rocks = [
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]],
    [[2, 2], [2, 1], [0, 0], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [0, 1], [1, 1]],
]


def collides(current: list[list], walls: set) -> bool:
    if any(y < 0 or x < 0 or x > 6 for x, y in current):
        return True

    return bool(set([tuple(part) for part in current]) & walls)


def update(current: list[list], walls: set) -> set:
    return set([tuple(part) for part in current]) | walls


def calc_highest(current: list[list], highest: int) -> int:
    return max(highest, *(y for _, y in current))


def calc_col_max(walls: set, highest: int) -> tuple:
    col_max = [10**8 for _ in range(7)]
    for x, y in walls:
        col_max[x] = min(highest - y, col_max[x])
    return tuple(col_max)


rock_total = 0
highest = -1
current = []
ticks = 0
walls = set()
wind_total = 0
prev = {}


while "poggers":
    if not current:
        current = deepcopy(rocks[rock_total % len(rocks)])
        for part in current:
            part[0] += 2
            part[1] += highest + 4

        ticks = 0
        rock_total += 1
        continue

    next = deepcopy(current)
    if ticks % 2 == 0:
        delta = winds[wind_total % len(winds)]
        for part in next:
            part[0] += delta

        wind_total += 1
    else:
        for part in next:
            part[1] -= 1

    collision = collides(next, walls)

    # if we went down
    if collision and ticks % 2 == 1:
        walls = update(current, walls)
        highest = calc_highest(current, highest)
        col_max = calc_col_max(walls, highest)
        sig = (col_max, wind_total % len(winds))
        if rock_total == 2022:
            print("Part 1:", highest + 1)

        if sig in prev:
            prev_highest, prev_rock_i = prev[sig]
            hdiff = highest - prev_highest
            rock_diff = rock_total - prev_rock_i
            xd = 1000000000000
            remaining = xd - prev_rock_i
            if remaining % rock_diff == 0:
                cycles = remaining // rock_diff
                print("Part 2:", prev_highest + cycles * hdiff + 1)
                break
        else:
            prev[sig] = (highest, rock_total)

        current = []
        ticks += 1
        continue

    if not collision:
        current = next

    ticks += 1
