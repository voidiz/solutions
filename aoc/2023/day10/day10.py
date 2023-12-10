import sys

lines = [line for line in sys.stdin.read().splitlines()]
S = 0, 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            S = (x, y)


def get_neighbors(x, y):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= ny < len(lines) and 0 <= nx < len(lines[0]):
            c = lines[y][x]
            nc = lines[ny][nx]

            if (c == "|" or nc == "|") and dy not in [
                -1,
                1,
            ]:
                continue

            if (c == "-" or nc == "-") and dx not in [
                -1,
                1,
            ]:
                continue

            if c == "L" and not (dx == 1 or dy == -1):
                continue

            if nc == "L" and not (dx == -1 or dy == 1):
                continue

            if c == "J" and not (dx == -1 or dy == -1):
                continue

            if nc == "J" and not (dx == 1 or dy == 1):
                continue

            if c == "7" and not (dx == -1 or dy == 1):
                continue

            if nc == "7" and not (dx == 1 or dy == -1):
                continue

            if c == "F" and not (dx == 1 or dy == 1):
                continue

            if nc == "F" and not (dx == -1 or dy == -1):
                continue

            if nc == ".":
                continue

            neighbors.append((nx, ny))

    return neighbors


def part1():
    q = [S]
    dist = {S: 0}
    visited = set([S])

    while q:
        x, y = q.pop(0)

        for nx, ny in get_neighbors(x, y):
            if (nx, ny) not in visited:
                q.append((nx, ny))
                dist[(nx, ny)] = dist[(x, y)] + 1
                visited.add((nx, ny))

    print("Part 1:", max(v for v in dist.values()))


def flood_fill(x, y, grid, vis):
    hit_edge = False
    vis.add((x, y))
    q = [(x, y)]

    filled = 0
    while q:
        # the grid is double resolution, so only count even tiles
        if x % 2 == 0 and y % 2 == 0:
            filled += 1

        x, y = q.pop(0)

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                hit_edge = True

            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                nc = grid[ny][nx]

                if nc == "." and (nx, ny) not in vis:
                    vis.add((nx, ny))
                    q.append((nx, ny))

    return hit_edge, filled


def construct_grid():
    grid = [
        ["." for _ in range(len(lines[0]) * 2)] for _ in range(len(lines) * 2)
    ]
    grid[S[1] * 2][S[0] * 2] = "S"

    vis = set()
    vis.add(S)

    q = [S]

    while q:
        x, y = q.pop(0)

        for nx, ny in get_neighbors(x, y):
            gx = x * 2
            gy = y * 2
            gnx = nx * 2
            gny = ny * 2

            grid[gny][gnx] = lines[ny][nx]

            # we walked horizontally
            dx = nx - x
            if abs(dx) == 1:
                grid[gy][gx + dx] = "-"

            # we walked vertically
            dy = ny - y
            if abs(dy) == 1:
                grid[gy + dy][gx] = "|"

            if (nx, ny) not in vis:
                q.append((nx, ny))
                vis.add((nx, ny))

    return grid


def part2():
    vis = set()
    grid = construct_grid()
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in vis or grid[y][x] != ".":
                continue

            hit_edge, filled = flood_fill(x, y, grid, vis)
            if not hit_edge:
                total += filled

    print("Part 2:", total)


part1()
part2()
