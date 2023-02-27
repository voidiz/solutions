import sys


lines = [line for line in sys.stdin.read().splitlines()]

part1 = 0
part2 = 0
for line in lines:
    p1, p2 = line.split(",")
    p11, p12 = map(int, p1.split("-"))
    p21, p22 = map(int, p2.split("-"))

    set1 = set(range(p11, p12 + 1))
    set2 = set(range(p21, p22 + 1))

    # or just
    # if p11 <= p21 and p22 <= p12 or p21 <= p11 and p12 <= p22:
    if set1.issubset(set2) or set2.issubset(set1):
        part1 += 1

    # or just
    # if not (p12 < p21 or p11 > p22):
    # = invert the condition of the ranges **not** overlapping
    if set1 & set2:
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
