import sys

ranges, ingredients = sys.stdin.read().split("\n\n")

R = []

for r in ranges.splitlines():
    s, e = map(int, r.split("-"))
    R.append([int(s), int(e)])


p1 = 0
for i in ingredients.splitlines():
    for s, e in R:
        if s <= int(i) <= e:
            p1 += 1
            break


print("Part 1:", p1)

R.sort()
merged = [R[0]]
for s, e in R[1:]:
    prev = merged[-1]
    if e <= prev[1]:
        continue

    if s <= prev[1]:
        merged[-1] = (prev[0], e)
        continue

    merged += [(s, e)]

p2 = 0
for s, e in merged:
    p2 += e - s + 1

print("Part 2:", p2)
