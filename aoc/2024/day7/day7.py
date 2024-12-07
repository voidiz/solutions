import sys

lines = sys.stdin.read().splitlines()

all_nums = []


def search(tar, tot, i, num_index, part2):
    nums = all_nums[num_index]
    if i == len(nums):
        if tot == tar:
            return 1

        return 0

    found = 0
    found += search(tar, tot + nums[i], i + 1, num_index, part2)
    found += search(tar, max(tot, 1) * nums[i], i + 1, num_index, part2)

    if part2:
        found += search(
            tar, int(str(tot) + str(nums[i])), i + 1, num_index, part2
        )

    return found


p1 = 0
p2 = 0
for i, line in enumerate(lines):
    target, rest = line.split(": ")
    target = int(target)
    rest = [int(x) for x in rest.split(" ")]
    all_nums.append(rest)

    res = search(target, 0, 0, i, False)
    if res > 0:
        p1 += target

    res = search(target, 0, 0, i, True)
    if res > 0:
        p2 += target

print("Part 1:", p1)
print("Part 2:", p2)
