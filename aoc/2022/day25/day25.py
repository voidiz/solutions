import sys

lines = [line for line in sys.stdin.read().splitlines()]


def dec(line):
    total = 0
    for i, c in enumerate(line):
        power = 5 ** (len(line) - i - 1)
        if c == "=":
            c = -2
        elif c == "-":
            c = -1
        else:
            c = int(c)
        total += c * power
    return total


p1 = sum(dec(line) for line in lines)


def snafu(total):
    if total == 0:
        return []

    rem = total % 5
    if rem == 3:  # -2 % 5 == 3
        return ["="] + snafu((total + 2) // 5)

    if rem == 4:  # -1 % 5 == 4
        return ["-"] + snafu((total + 1) // 5)

    return [str(rem)] + snafu(total // 5)


print("Part 1:", "".join(snafu(p1)[::-1]))
