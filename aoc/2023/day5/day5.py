import sys

parts = sys.stdin.read().split("\n\n")
seeds = list(map(int, parts[0].split(": ")[1].split()))
maps = []

for part in parts[1:]:
    part_list = []
    part_lines = part.splitlines()
    for line in part_lines[1:]:
        part_list.append(list(map(int, line.split())))

    maps.append(part_list)


p1 = 10**12
for val in seeds:
    for m in maps:
        for dst, src, length in m:
            if src < val <= src + length:
                val = val - src + dst
                break

    p1 = min(p1, val)

print("Part 1:", p1)


def get_intervals(intervals, m):
    inside = []
    for dst, src, length in m:
        outside = []

        # partition all intervals into intervals that
        # are inside [src, src + length) and outside
        while intervals:
            l, r = intervals.pop()

            # [ll, lr)...[il, ir)...[rl, rr)
            # where [il, ir) is inside [src, src + length)
            # and [ll, lr), [rl, rr) are outside
            ll = l
            lr = min(r, src)
            il = max(l, src)
            ir = min(r, src + length)
            rl = max(l, src + length)
            rr = r

            if ll < lr:
                outside.append((ll, lr))

            if il < ir:
                inside.append((il - src + dst, ir - src + dst))

            if rl < rr:
                outside.append((rl, rr))

        # try the intervals outside with the other mappings
        intervals = outside

    return inside + intervals


p2 = []
for seed, length in list(zip(seeds[::2], seeds[1::2])):
    intervals = [(seed, seed + length)]
    for m in maps:
        intervals = get_intervals(intervals, m)

    p2 += intervals

print("Part 2:", min(p2)[0])
