import sys
import functools

from collections import deque

lines = sys.stdin.read().splitlines()

num_keypad = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    (0, 2): "1",
    (1, 2): "2",
    (2, 2): "3",
    (1, 3): "0",
    (2, 3): "A",
}

dir_keypad = {
    (1, 0): "^",
    (2, 0): "A",
    (0, 1): "<",
    (1, 1): "v",
    (2, 1): ">",
}


@functools.cache
def shortest_num_path(sx, sy, ex, ey, robots):
    q = deque([(sx, sy, "")])
    vis = set()
    best = 10**12
    while q:
        x, y, p = q.popleft()
        vis.add((x, y))

        if (x, y) == (ex, ey):
            best = min(best, shortest_dir_path(p + "A", robots))
            continue

        for dx, dy, dd in [
            (-1, 0, "<"),
            (1, 0, ">"),
            (0, 1, "v"),
            (0, -1, "^"),
        ]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in num_keypad and (nx, ny) not in vis:
                q += [(nx, ny, p + dd)]

    return best


@functools.cache
def shortest_dir_path(dirs, robots):
    if robots == 1:
        return len(dirs)

    tot = 0
    sx, sy = 2, 0
    for d in dirs:
        ex, ey = next(e for e, v in dir_keypad.items() if v == d)
        q = deque([(sx, sy, "")])
        vis = set()
        best = 10**12
        while q:
            x, y, p = q.popleft()
            vis.add((x, y))

            if (x, y) == (ex, ey):
                best = min(best, shortest_dir_path(p + "A", robots - 1))
                continue

            for dx, dy, dd in [
                (-1, 0, "<"),
                (1, 0, ">"),
                (0, 1, "v"),
                (0, -1, "^"),
            ]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in dir_keypad and (nx, ny) not in vis:
                    q += [(nx, ny, p + dd)]

        tot += best
        sx, sy = ex, ey

    return tot


p1 = 0
p2 = 0
for line in lines:
    sx, sy = 2, 3
    num = int(line[:-1])
    for c in line:
        ex, ey = next(s for s, v in num_keypad.items() if v == c)
        p1 += num * shortest_num_path(sx, sy, ex, ey, 3)
        p2 += num * shortest_num_path(sx, sy, ex, ey, 26)
        sx, sy = ex, ey

print("Part 1:", p1)
print("Part 2:", p2)
