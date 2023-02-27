import dataclasses
import sys
import re
import functools
import math

from typing import Callable

monkey_parts = [line for line in sys.stdin.read().split("\n\n")]


@dataclasses.dataclass
class Monkey:
    items: list[int]
    test: int
    t: int
    f: int
    op: Callable[[int], int]
    inspections: int = 0

    def __iter__(self):
        # To allow for shallow unpacking since dataclasses.astuple
        # performs a deepcopy which is very costly...
        return iter(self.__dict__.values())


def parse() -> tuple[list[Monkey], int]:
    # Only need to keep track of worry factors mod
    # the lcm of all test numbers.
    # However, all inputs seem to be prime anyway,
    # so the product should be just as good
    test_factor = 1

    monkeys = []
    for monkey in monkey_parts:
        lines = monkey.split("\n")
        items = list(map(int, re.findall(r"\d+", lines[1])))
        test, t, f = map(int, re.findall(r"\d+", "\n".join(lines[3:])))
        opline = lines[2].split(" ")

        def op(opline: list[str], item: int) -> int:
            # old must be here since it's used in eval :)
            old = item
            return eval("".join(opline[5:]))

        monkeys.append(
            Monkey(items, test, t, f, functools.partial(op, opline))
        )
        test_factor = math.lcm(test, test_factor)

    return monkeys, test_factor


def solve(rounds: int, part2=False) -> int:
    monkeys, test_factor = parse()
    for _ in range(rounds):
        for monkey in monkeys:
            items, test, t, f, op, _ = monkey
            monkey.inspections += len(monkey.items)

            for item in items:
                res = op(item)
                worry = res % test_factor if part2 else res // 3
                if worry % test == 0:
                    monkeys[t].items.append(worry)
                else:
                    monkeys[f].items.append(worry)

            monkey.items = []

    *_, second, first = sorted([monkey.inspections for monkey in monkeys])
    return second * first


print("Part 1:", solve(20))
print("Part 2:", solve(10000, True))
