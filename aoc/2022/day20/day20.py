import sys

gid = 0
lines = [int(line) for line in sys.stdin.read().splitlines()]
items = []
for i, line in enumerate(lines):
    items.append((line, gid))
    gid += 1


def mix(items, times=1):
    initial = items.copy()
    for _ in range(times):
        for num, id in initial:
            idx = -1
            for i in range(len(items)):
                if items[i][1] == id:
                    idx = i
            assert id != -1

            items.pop(idx)
            new_i = (idx + num) % len(items)

            if new_i == 0:
                items.append((num, id))
            else:
                items.insert(new_i, (num, id))

    return items


def calc(items):
    for i, (num, *_) in enumerate(items):
        if num == 0:
            return sum(
                (
                    items[(i + 1000) % len(items)][0],
                    items[(i + 2000) % len(items)][0],
                    items[(i + 3000) % len(items)][0],
                )
            )


p1 = mix(items.copy())
print("Part 1:", calc(p1))
p2 = mix([(item * 811589153, id) for item, id in items], 10)
print("Part 2:", calc(p2))
