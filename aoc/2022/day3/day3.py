import sys

lines = sys.stdin.read().splitlines()


def calculate_score(shares: str) -> int:
    return (
        ord(shares) - ord("A") + 1 + 26
        if shares.isupper()
        else ord(shares) - ord("a") + 1
    )


part1 = 0
for line in lines:
    half = len(line) // 2
    shares = (set(line[:half]) & set(line[half:])).pop()
    part1 += calculate_score(shares)

part2 = 0
for i in range(0, len(lines), 3):
    shares = (set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])).pop()
    part2 += calculate_score(shares)

print("Part 1:", part1)
print("Part 2:", part2)
