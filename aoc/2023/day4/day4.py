import sys

lines = [line for line in sys.stdin.read().splitlines()]

cards = []
for line in lines:
    l, r = line.split("|")
    l = l.split(": ")[1].split()
    r = r[1:].split()

    l = set(l)
    r = set(r)

    cards.append((l, r))


total = 0
for l, r in cards:
    matches = 0
    for item in l:
        if item in r:
            if matches > 1:
                matches *= 2
            else:
                matches += 1

    total += matches

print("Part 1:", total)

total = 0
repeats = [1] * len(lines)
for i, (l, r) in enumerate(cards):
    matches = len(l & r)

    for j in range(i + 1, i + 1 + matches):
        repeats[j] += repeats[i]


print("Part 2:", sum(repeats))
