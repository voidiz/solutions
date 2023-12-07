import sys
import re

lines = [line.strip() for line in sys.stdin.read().splitlines()]

total = 0
for line in lines:
    num = ""
    for c in line:
        if c.isnumeric():
            num += c
            break

    for c in line[::-1]:
        if c.isnumeric():
            num += c
            break

    if num.isnumeric():
        total += int(num)

print("Part 1:", total)

total = 0
for line in lines:
    res = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    dct = {
        item: str(i + 1)
        for i, item in enumerate(
            [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
        )
    }

    for i in range(1, 10):
        dct[str(i)] = str(i)

    num = ""
    if res[0].isnumeric():
        num += res[0]
    else:
        num += dct[res[0]]

    if res[-1].isnumeric():
        num += res[-1]
    else:
        num += dct[res[-1]]

    total += int(num)

print("Part 2:", total)
