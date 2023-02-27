import sys

lines = [line for line in sys.stdin.read().splitlines()]

tree = {}
cwd = []
p2 = 0


def size(tree: dict) -> int:
    if isinstance(tree, int):
        return tree

    return sum(size(tree[k]) for k in tree)


def traverse(tree: dict, tree_size: int) -> int:
    if isinstance(tree, int):
        return 0

    sz = size(tree)

    # Part 2 stuff
    global p2
    free_space = 70000000 - tree_size
    target = 30000000
    target_diff = abs(free_space - target)
    diff = abs(p2 - target_diff)
    new_diff = abs(sz - target_diff)
    if new_diff < diff:
        p2 = sz

    # Part 1
    rest = sum(traverse(tree[sub], tree_size) for sub in tree)
    if sz <= 100000:
        return sz + rest

    return rest


def index(stack: list[str], current: dict) -> dict:
    if not stack:
        return current

    if stack[0] not in current:
        current[stack[0]] = {}

    return index(stack[1:], current[stack[0]])


for line in lines:
    args = line.split(" ")
    if line.startswith("$ cd"):
        cmd = args[1]
        path = args[2]
        if path == "..":
            cwd.pop()
            continue

        if path == "/":
            cwd = ["/"]
            continue

        cwd.append(path)

    c = index(cwd, tree)
    if args[0].isnumeric():
        c[args[1]] = int(args[0])

print("Part 1:", traverse(tree, size(tree)))
print("Part 2:", p2)
