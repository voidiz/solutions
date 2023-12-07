import sys

from collections import defaultdict

lines = [line for line in sys.stdin.read().splitlines()]


total = 0
for y, line in enumerate(lines):
    num = ""
    part = False
    for x, c in enumerate(line):
        if c.isdigit():
            num += c
        else:
            if part and num:
                total += int(num)

            part = False
            num = ""
            continue

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(line) and 0 <= ny < len(lines):
                    if lines[ny][nx] != "." and not lines[ny][nx].isdigit():
                        part = True
                        break

    if part and num:
        total += int(num)

    part = False
    num = ""

print("Part 1:", total)

total = 0
gears = defaultdict(list)
for y, line in enumerate(lines):
    num = ""
    part = tuple()
    for x, c in enumerate(line):
        if c.isdigit():
            num += c
        else:
            if part and num:
                gears[part].append(int(num))

            part = tuple()
            num = ""
            continue

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(line) and 0 <= ny < len(lines):
                    if str(lines[ny][nx]) == "*":
                        part = (ny, nx)
                        break

    if part and num:
        gears[part].append(int(num))

    part = False
    num = ""

for nums in gears.values():
    if len(nums) == 2:
        total += nums[0] * nums[1]

print("Part 2:", total)
