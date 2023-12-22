import sys
import functools

from dataclasses import dataclass

lines = [line for line in sys.stdin.read().splitlines()]


@dataclass
class Brick:
    start: list
    end: list

    def collide(self, other):
        (aminx, aminy, aminz), (amaxx, amaxy, amaxz) = self.start, self.end
        (bminx, bminy, bminz), (bmaxx, bmaxy, bmaxz) = other.start, other.end

        return (
            aminx <= bmaxx
            and amaxx >= bminx
            and aminy <= bmaxy
            and amaxy >= bminy
            and aminz <= bmaxz
            and amaxz >= bminz
        )

    def move_down(self):
        self.start[2] -= 1
        self.end[2] -= 1

    def move_up(self):
        self.start[2] += 1
        self.end[2] += 1


bricks = []
for line in lines:
    start, end = line.split("~")
    start = list(map(int, start.split(",")))
    end = list(map(int, end.split(",")))
    bricks.append(Brick(start, end))


bricks.sort(key=functools.cmp_to_key(lambda a, b: a.start[2] - b.start[2]))


def is_valid(brick_idx, bricks):
    if bricks[brick_idx].start[2] < 1:
        return False

    # bricks is sorted by z, so only check same z or lower
    for i in range(brick_idx):
        if bricks[brick_idx].collide(bricks[i]):
            return False

    return True


def move_bricks(bricks, early_stop=False):
    moved = True
    fell = set()
    while moved:
        moved = False

        for i, brick in enumerate(bricks):
            brick.move_down()
            if is_valid(i, bricks):
                moved = True
                fell.add(i)
            else:
                brick.move_up()

        if early_stop:
            break

    return fell


move_bricks(bricks)

p1 = 0
p2 = 0
for i, brick in enumerate(bricks):
    removed = bricks.pop(i)
    fell = move_bricks(bricks, True)

    if not fell:
        p1 += 1

    p2 += len(fell)

    # reverse everything
    for bi in fell:
        bricks[bi].move_up()

    bricks.insert(i, removed)

print("Part 1:", p1)
print("Part 2:", p2)
