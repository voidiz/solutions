import sys
import functools

lines = [line for line in sys.stdin.read().splitlines()]


def solve(part2):
    total = 0

    for line in lines:
        arr, amount = line.split(" ")

        if part2:
            arr = "?".join([arr] * 5)
            amount = ",".join([amount] * 5)

        amount = list(map(int, amount.split(",")))

        @functools.cache
        def search(i, collected, needed):
            if i == len(arr):
                if len(needed) == 1 and collected == needed[0]:
                    return 1

                if not needed and collected == 0:
                    return 1

                return 0

            if arr[i] == "#":
                return search(i + 1, collected + 1, needed)

            if arr[i] == ".":
                if collected == 0:
                    return search(i + 1, 0, needed)

                if needed and collected == needed[0]:
                    return search(i + 1, 0, needed[1:])

            if arr[i] == "?":
                total = 0

                # set ? -> #
                if needed:
                    total += search(i + 1, collected + 1, needed)

                # set ? -> .
                if collected == 0:
                    total += search(i + 1, 0, needed)
                elif needed and collected == needed[0]:
                    total += search(i + 1, 0, needed[1:])

                return total

            return 0

        total += search(0, 0, tuple(amount))

    return total


print("Part 1:", solve(False))
print("Part 2:", solve(True))
