import sys

rrs, prog = sys.stdin.read().split("\n\n")
rrs = rrs.splitlines()
prog = [int(x) for x in prog.strip().split(" ")[1].split(",")]

regs = {}

for line in rrs:
    r, num = line.split(": ")
    r = r.split(" ")[1]
    num = int(num)
    regs[r] = num


def get_combo(num):
    if num in range(0, 4):
        return num

    if num == 4:
        return regs["A"]

    if num == 5:
        return regs["B"]

    if num == 6:
        return regs["C"]

    raise ValueError("invalid op " + num)


def run(prog, regs):
    ip = 0
    output = []
    while ip < len(prog) - 1:
        inst = prog[ip]
        oper = prog[ip + 1]
        if inst == 0:
            regs["A"] = regs["A"] // (2 ** get_combo(oper))
        elif inst == 1:
            regs["B"] = oper ^ regs["B"]
        elif inst == 2:
            regs["B"] = get_combo(oper) % 8
        elif inst == 3:
            if regs["A"] != 0:
                ip = oper
                continue
        elif inst == 4:
            regs["B"] = regs["B"] ^ regs["C"]
        elif inst == 5:
            output.append(get_combo(oper) % 8)
        elif inst == 6:
            regs["B"] = regs["A"] // (2 ** get_combo(oper))
        elif inst == 7:
            regs["C"] = regs["A"] // (2 ** get_combo(oper))

        ip += 2

    return output, output[:7] == prog[:7]


print("Part 1:", ",".join(str(n) for n in run(prog, regs)[0]))

a = 1
prev = 1
prev_output = []
found_start = False
diff = 1
while True:
    regs["A"] = a
    output, same_prefix = run(prog, regs)

    if same_prefix and output != prev_output and diff == 1:
        if found_start:
            diff = a - prev

        found_start = True
        prev = a
        prev_output = output

    if len(output) != len(prog):
        a *= 2
        continue

    if output == prog:
        print("Part 2:", a)
        break

    if diff == 1:
        a += 1
    elif output[-3:-1] == prog[-3:-1]:
        a += diff
    elif output[-4:-2] == prog[-4:-2]:
        a += diff * 10
    else:
        a += diff * 100
