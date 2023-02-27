import sys

from collections import defaultdict, deque

lines = [line for line in sys.stdin.read().splitlines()]

elves = set()


for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            elves.add((j, i))

pol = {
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1),
}


def print_elves():
    xs, ys = zip(*elves)
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    grid = [
        ["." for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)
    ]

    for x, y in elves:
        grid[y - miny][x - minx] = "#"

    print("\n".join("".join(row) for row in grid))


def get_occ(pos):
    x, y = pos
    occ = []

    for dx, dy in pol.values():
        nx, ny = x + dx, y + dy
        if (nx, ny) in elves:
            occ.append((dx, dy))

    return occ


# set and dxdy
dirs = deque(
    [
        (set((pol[p] for p in ("N", "NE", "NW"))), (0, -1)),
        (set((pol[p] for p in ("S", "SE", "SW"))), (0, 1)),
        (set((pol[p] for p in ("W", "NW", "SW"))), (-1, 0)),
        (set((pol[p] for p in ("E", "NE", "SE"))), (1, 0)),
    ]
)

rounds = 1
while "poggers":
    new_elves = defaultdict(int)
    to_remove = {}
    moved = False
    for elf in elves.copy():
        occ = set(get_occ(elf))
        if not occ:
            continue

        moved = True

        x, y = elf
        for dirset, (dx, dy) in dirs:
            if not (dirset & occ):
                nx, ny = x + dx, y + dy
                new_elves[(nx, ny)] += 1
                to_remove[(nx, ny)] = elf
                break

    for new_elf, amn in new_elves.items():
        if amn == 1:
            elves.add(new_elf)
            elves.remove(to_remove[new_elf])

    first = dirs.popleft()
    dirs.append(first)

    if rounds == 10:
        xs, ys = zip(*elves)
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)

        empty = 0
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                if (x, y) not in elves:
                    empty += 1

        print("Part 1:", empty)

    if not moved:
        print("Part 2:", rounds)
        break

    rounds += 1
