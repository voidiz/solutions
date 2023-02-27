import sys

groups = [group for group in sys.stdin.read().split("\n\n")]
totals = sorted(
    [
        sum([int(line) for line in group.split("\n") if line])
        for group in groups
    ]
)

print("Part 1:", totals[-1])
print("Part 2:", sum(totals[-3:]))
