import sys
from collections import defaultdict


line = sys.stdin.read().strip()

seq = line.split(",")


def hash(label):
    total = 0
    for c in label:
        total += ord(c)
        total *= 17
        total = total % 256

    return total


p1 = sum(hash(step) for step in seq)
print("Part 1:", p1)


boxes = defaultdict(list)
for step in seq:
    if "=" in step:
        label, num = step.split("=")
        hashed = hash(label)
        for i in range(len(boxes[hashed])):
            lbl, n = boxes[hashed][i]
            if label == lbl:
                boxes[hashed][i] = (label, num)
                break
        else:
            boxes[hashed].append((label, num))

    elif "-" in step:
        label = step[:-1]
        hashed = hash(label)
        boxes[hashed] = [
            (lbl, num) for lbl, num in boxes[hashed] if lbl != label
        ]


p2 = 0
for num, lst in boxes.items():
    p2 += (num + 1) * sum(
        (i + 1) * int(focal) for i, (_, focal) in enumerate(lst)
    )

print("Part 2:", p2)
