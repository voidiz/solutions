import sys

from copy import deepcopy

lines = [list(line) for line in sys.stdin.read().splitlines()]


def is_free(x, y, dx, dy, lines):
    if 0 <= x + dx < len(lines[0]) and 0 <= y + dy < len(lines):
        return lines[y + dy][x + dx] == "."
    return False


def step(dx, dy, lines):
    new_lines = deepcopy(lines)
    moved = False
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != "O":
                continue

            if is_free(x, y, dx, dy, lines):
                new_lines[y + dy][x + dx] = "O"
                new_lines[y][x] = "."
                moved = True

    return new_lines, moved


def calc_load(lines):
    total = 0
    for i, line in enumerate(lines):
        for c in line:
            if c == "O":
                total += len(lines) - i
    return total


new_lines = lines
cycle_lines = [lines]
while True:
    for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        while True:
            new_lines, moved = step(dx, dy, new_lines)
            if not moved:
                if len(cycle_lines) == 1 and dy == -1:
                    print("Part 1:", calc_load(new_lines))
                break

    if new_lines in cycle_lines:
        cycle_start = cycle_lines.index(new_lines)
        cycle_end = len(cycle_lines)
        cycle_length = cycle_end - cycle_start
        idx = cycle_start + ((1000000000 - cycle_start) % (cycle_length))
        print("Part 2:", calc_load(cycle_lines[idx]))
        break

    cycle_lines.append(new_lines)
