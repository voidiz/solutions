import sys

lines = [line for line in sys.stdin.read().splitlines()]


dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
q: list[tuple[int, int]] = [(0, 0) for _ in range(10)]
p1 = set()
p2 = set()

for line in lines:
    dir, step = line.split(" ")
    step = int(step)
    for _ in range(step):
        hx, hy = q[0]
        dx, dy = dirs[dir]

        hx += dx
        hy += dy

        q[0] = (hx, hy)
        for i in range(len(q[:-1])):
            ax, ay = q[i]
            bx, by = q[i + 1]
            if abs(ax - bx) >= 2 or abs(ay - by) >= 2:
                nx = bx
                ny = by
                if ax > bx:
                    nx += 1
                if bx > ax:
                    nx -= 1

                if ay > by:
                    ny += 1
                if by > ay:
                    ny -= 1

                q[i + 1] = (nx, ny)

        p1.add(q[1])
        p2.add(q[-1])

print("Part 1:", len(p1))
print("Part 2:", len(p2))
