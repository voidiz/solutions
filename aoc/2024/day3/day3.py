import sys
import re

line = sys.stdin.read()

p1 = 0
p2 = 0
matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", line)
enabled = True
for m in matches:
    x, y, do, dont = m

    if do:
        enabled = True

    if dont:
        enabled = False

    if x and y:
        if enabled:
            p2 += int(x) * int(y)

        p1 += int(x) * int(y)

print("Part 1:", p1)
print("Part 2:", p2)
