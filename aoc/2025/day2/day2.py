import sys

lines = [line for line in sys.stdin.read().splitlines()]


def check_dup(s, seq, p2):
    i = 0
    reps = 0

    while i < len(s):
        if s[i : i + len(seq)] != seq:
            return False

        i += len(seq)
        reps += 1

    if p2:
        return reps >= 2 and i == len(s)

    return reps == 2 and i == len(s)


def solve(p2):
    invalid_ids = set()
    for r in lines[0].split(","):
        left, right = map(int, r.split("-"))

        for id in range(left, right + 1):
            for i in range(1, len(str(id))):
                part = str(id)[:i]
                if check_dup(str(id), part, p2):
                    invalid_ids.add(id)

    return sum(invalid_ids)


print("Part 1:", solve(False))
print("Part 2:", solve(True))
