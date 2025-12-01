import sys

lines = [line for line in sys.stdin.read().splitlines()]

dial = 50
p1 = 0
p2 = 0

for line in lines:
    t = int(line[1:])
    if line[0] == "R":
        for _ in range(t):
            dial = (dial + 1) % 100
            if dial == 0:
                p2 += 1
    else:
        for _ in range(t):
            dial = (dial - 1) % 100
            if dial == 0:
                p2 += 1

    if dial == 0:
        p1 += 1

print("Part 1:", p1)
print("Part 2:", p2)
