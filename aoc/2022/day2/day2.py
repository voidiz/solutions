import sys

lines = [line for line in sys.stdin.read().splitlines()]

scores = {"X": 1, "Y": 2, "Z": 3}

part1 = 0
part2 = 0
for line in lines:
    elf, me = line.split(" ")
    if elf == "A":
        if me == "Y":
            part1 += 6
        if me == "X":
            part1 += 3

    if elf == "B":
        if me == "Z":
            part1 += 6
        if me == "Y":
            part1 += 3

    if elf == "C":
        if me == "X":
            part1 += 6
        if me == "Z":
            part1 += 3

    part1 += scores[me]

    # A = rock, B = paper, C = scissors
    # X = rock, Y = paper, Z = scissors
    # Y = draw, X = lose, Z = win
    if elf == "A":
        if me == "Y":
            part2 += scores["X"] + 3
        if me == "X":
            part2 += scores["Z"]
        if me == "Z":
            part2 += scores["Y"] + 6

    if elf == "B":
        if me == "Y":
            part2 += scores["Y"] + 3
        if me == "X":
            part2 += scores["X"]
        if me == "Z":
            part2 += scores["Z"] + 6

    if elf == "C":
        if me == "Y":
            part2 += scores["Z"] + 3
        if me == "X":
            part2 += scores["Y"]
        if me == "Z":
            part2 += scores["X"] + 6

print("Part 1:", part1)
print("Part 2:", part2)
