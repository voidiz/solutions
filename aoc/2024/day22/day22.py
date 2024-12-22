import sys

from collections import Counter

lines = [int(line) for line in sys.stdin.read().splitlines()]


def secrets(num, rem):
    ss = [num]

    for _ in range(rem):
        to_mix = num * 64
        num ^= to_mix
        num %= 16777216

        to_mix = num // 32
        num ^= to_mix
        num %= 16777216

        to_mix = num * 2048
        num ^= to_mix
        num %= 16777216

        ss += [num]

    return ss


def diffs(ss):
    ds = []
    prices = {}

    for ps, s in zip(ss, ss[1:]):
        ds += [s % 10 - ps % 10]
        seq = tuple(ds[-4:])

        if len(seq) == 4 and seq not in prices:
            prices[seq] = s % 10

    return prices


p1 = 0
p2 = Counter()
for line in lines:
    num = line
    ss = secrets(num, 2000)
    p1 += ss[-1]
    p2 += diffs(ss)

print("Part 1:", p1)
print("Part 2:", p2.most_common(1)[0][1])
