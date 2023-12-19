import sys
import re

workflows, ratings = sys.stdin.read().split("\n\n")
workflows = workflows.splitlines()
ratings = ratings.splitlines()

wfs = {}
for w in workflows:
    id, rest = w.split("{")
    wfs[id] = rest[:-1].split(",")


# lbl, lt, num, true_lbl
def parse_condition(condition):
    match = re.match(r"(\w)(>|<)(\d+):(\w+)", condition)
    assert match

    var, op, num, true_lbl = match.groups()
    return var, op == "<", int(num), true_lbl


def accepted(lbl, rating):
    if lbl == "A":
        return True

    if lbl == "R":
        return False

    for wf in wfs[lbl]:
        if ":" not in wf:
            return accepted(wf, rating)

        cond, true_lbl = wf.split(":")

        exec(rating.strip())
        if eval(cond):
            return accepted(true_lbl, rating)

    assert False and "impossible"


# lt == var < num
def update_ranges(var, lt, num, ranges):
    var_idx = "xmas".index(var)

    new_ranges = []
    for r in ranges:
        new_range = []
        for i, (l, u) in enumerate(r):
            if i != var_idx:
                new_range.append((l, u))
                continue

            if lt:
                # var < num, update upper limit
                u = min(u, num - 1)
            else:
                # num < var, update lower limit
                l = max(l, num + 1)

            # invalid range, no point in continuing
            if l > u:
                break

            new_range.append((l, u))
        else:
            new_ranges.append(new_range)

    return new_ranges


# find all valid ranges
def search(conditions):
    # current: condition, workflow label or A/R
    current = conditions[0]

    if current == "A":
        # base case; all valid
        return [[(1, 4000) for _ in range(4)]]

    if current == "R":
        # base case, no valid ranges
        return []

    if ":" not in current:
        # not a condition, just continue search
        return search(wfs[current])

    var, lt, num, true_lbl = parse_condition(current)

    # current is a condition, so we need to branch on true/false
    # case: true
    true_rest = search([true_lbl])
    true_ranges = update_ranges(var, lt, num, true_rest)

    # case: false
    false_rest = search(conditions[1:])

    # adjust num so it includes equality
    false_num = num - 1 if lt else num + 1
    false_ranges = update_ranges(var, not lt, false_num, false_rest)

    return true_ranges + false_ranges


p1 = 0
for rating in ratings:
    if accepted("in", rating[1:-1].replace(",", ";")):
        p1 += sum(map(int, re.findall(r"\d+", rating)))

print("Part 1:", p1)

p2 = 0
for r in search(["in"]):
    total = 1
    for l, u in r:
        total *= u - l + 1

    p2 += total

print("Part 2:", p2)
