import sys
import re
import functools

lines = [line for line in sys.stdin.read().splitlines()]

p1 = 0
p2 = 1
for line in lines:
    (
        id,
        ore_cost,
        clay_ore_cost,
        obsidian_ore,
        obsidian_clay,
        geode_ore,
        geode_obsidian,
    ) = map(int, re.findall(r"-?\d+", line))

    max_ore_cost = max(ore_cost, clay_ore_cost, obsidian_ore, geode_ore)
    max_clay_cost = obsidian_clay
    max_obsidian_cost = geode_obsidian

    @functools.cache
    def explore(
        remaining,
        ores,
        obsidian,
        clay,
        ore_robots,
        clay_robots,
        obsidian_robots,
        geode_robots,
    ):
        if remaining == 0:
            return 0

        ores += ore_robots
        clay += clay_robots
        obsidian += obsidian_robots

        if (
            ores - ore_robots >= geode_ore
            and obsidian - obsidian_robots >= geode_obsidian
        ):
            return geode_robots + explore(
                remaining - 1,
                ores - geode_ore,
                obsidian - geode_obsidian,
                clay,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots + 1,
            )

        best = 0

        if ores - ore_robots >= ore_cost and ore_robots < max_ore_cost:
            best = max(
                best,
                explore(
                    remaining - 1,
                    ores - ore_cost,
                    obsidian,
                    clay,
                    ore_robots + 1,
                    clay_robots,
                    obsidian_robots,
                    geode_robots,
                ),
            )

        if ores - ore_robots >= clay_ore_cost and clay_robots < max_clay_cost:
            best = max(
                best,
                explore(
                    remaining - 1,
                    ores - clay_ore_cost,
                    obsidian,
                    clay,
                    ore_robots,
                    clay_robots + 1,
                    obsidian_robots,
                    geode_robots,
                ),
            )

        if (
            ores - ore_robots >= obsidian_ore
            and clay - clay_robots >= obsidian_clay
            and obsidian_robots < max_obsidian_cost
        ):
            best = max(
                best,
                explore(
                    remaining - 1,
                    ores - obsidian_ore,
                    obsidian,
                    clay - obsidian_clay,
                    ore_robots,
                    clay_robots,
                    obsidian_robots + 1,
                    geode_robots,
                ),
            )

        if ores - ore_robots < max_ore_cost:
            best = max(
                best,
                explore(
                    remaining - 1,
                    ores,
                    obsidian,
                    clay,
                    ore_robots,
                    clay_robots,
                    obsidian_robots,
                    geode_robots,
                ),
            )

        return best + geode_robots

    p1 += id * explore(
        24,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
    )

    if id < 4:
        p2 *= explore(
            32,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
        )

print("Part 1:", p1)
print("Part 2:", p2)
