import sys
import itertools

lines = [line for line in sys.stdin.read().splitlines()]


def safe(nums):
    diffs = [a - b for a, b in zip(nums, nums[1:])]

    inc = all(1 <= diff <= 3 for diff in diffs)
    dec = all(-3 <= diff <= -1 for diff in diffs)

    return inc or dec


p1 = 0
p2 = 0
for line in lines:
    nums = [int(x) for x in line.split()]

    # part 1
    if safe(nums):
        p1 += 1

    # part 2
    rem_one = list(itertools.combinations(nums, len(nums) - 1))
    if any(safe(report) for report in [nums] + rem_one):
        p2 += 1

print("Part 1:", p1)
print("Part 2:", p2)
