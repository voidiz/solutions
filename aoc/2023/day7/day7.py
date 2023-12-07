import sys
import functools

from collections import Counter

lines = [line for line in sys.stdin.read().splitlines()]


def get_type(a, part2):
    if part2 and a["J"] != 0:
        # special case, only J
        if a["J"] == 5:
            a["A"] = 5
        else:
            best_letter = max((v, k) for k, v in a.items() if k != "J")[1]
            a[best_letter] += a["J"]

        del a["J"]

    if any(v == 5 for v in a.values()):
        # 5 of a kind
        return 6

    if any(v == 4 for v in a.values()):
        # 4 of a kind
        return 5

    first, second, *_ = sorted(a.values())
    if first == 2 and second == 3:
        # full house
        return 4

    if any(v == 3 for v in a.values()):
        # three of a kind
        return 3

    *_, pair1, pair2 = sorted(a.values())
    if pair1 == 2 and pair2 == 2:
        # two pair
        return 2

    if pair2 == 2:
        # one pair
        return 1

    # high card
    return 0


strength1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
strength2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def cmp_part(part2):
    strength = strength2 if part2 else strength1

    def cmp(c1: Card, c2: Card):
        t1 = get_type(c1.amount, part2)
        t2 = get_type(c2.amount, part2)

        if t1 != t2:
            return t1 - t2

        # same type
        for i in range(5):
            i1 = strength.index(c1.hand[i])
            i2 = strength.index(c2.hand[i])

            if i1 != i2:
                return i2 - i1

        return 0

    return cmp


class Card:
    def __init__(self, line):
        hand, bid = line.split()
        self.hand = hand
        self.bid = int(bid)
        self.amount = Counter(hand)


cards = [Card(line) for line in lines]

p1_cards = sorted(cards, key=functools.cmp_to_key(cmp_part(False)))
p2_cards = sorted(cards, key=functools.cmp_to_key(cmp_part(True)))

p1 = 0
p2 = 0
for i in range(len(cards)):
    p1 += p1_cards[i].bid * (i + 1)
    p2 += p2_cards[i].bid * (i + 1)


print("Part 1:", p1)
print("Part 2:", p2)
