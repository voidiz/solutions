import sys

line = sys.stdin.read().strip()


def part1():
    grid = []
    for i, c in enumerate(line):
        c = int(c)
        if i % 2 == 0:
            grid += [i // 2] * c
        else:
            grid += ["."] * c

    for j, c in reversed(list(enumerate(grid))):
        if c == ".":
            continue

        for i in range(j):
            if grid[i] == ".":
                grid[i] = c
                grid[j] = "."
                break

    return sum(i * v for i, v in enumerate(grid) if v != ".")


def part2():
    grid = []
    spaces = []
    pos = 0
    for i, c in enumerate(line):
        c = int(c)
        if i % 2 == 0:
            grid.append((pos, pos + c, i // 2))
        else:
            spaces.append((pos, pos + c))

        pos += c

    result = {}
    for a, b, bid in reversed(grid):
        size = b - a
        found = False
        for i, (c, d) in enumerate(spaces):
            if b < c:
                continue

            space = d - c
            if space >= size:
                new_start = c + size
                spaces[i] = (new_start, d)
                result[(c, c + size)] = bid
                found = True
                break

        if not found:
            result[(a, b)] = bid

    p2 = 0
    for (a, b), bid in sorted(result.items()):
        for i in range(a, b):
            p2 += bid * i

    return p2


print("Part 1:", part1())
print("Part 2:", part2())
