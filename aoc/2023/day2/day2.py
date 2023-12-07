import sys

lines = [line for line in sys.stdin.read().splitlines()]

games = []

for line in lines:
    id, reveals = line.split(": ")
    _, id = id.split()

    reveals = [
        [col.split() for col in reveal.split(", ")]
        for reveal in reveals.split(";")
    ]

    games.append((id, reveals))


total = 0
for id, reveals in games:
    for reveal in reveals:
        r = 12
        g = 13
        b = 14

        for num, col in reveal:
            num = int(num)
            if col == "red":
                r -= num
            elif col == "green":
                g -= num
            elif col == "blue":
                b -= num

        if r < 0 or g < 0 or b < 0:
            break
    else:
        total += int(id)

print("Part 1:", total)


total = 0
for id, reveals in games:
    r = 0
    g = 0
    b = 0
    for reveal in reveals:
        for num, col in reveal:
            num = int(num)
            if col == "red":
                r = max(num, r)
            elif col == "green":
                g = max(num, g)
            elif col == "blue":
                b = max(num, b)

    total += r * g * b

print("Part 2", total)
