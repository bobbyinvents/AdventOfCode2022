content = [
    (i.split()[0], int(i.split()[-1])) if len(i.split()) == 2 else i
    for i in open("input.txt").read().strip().split("\n")
]

cycle, X = 0, 1
signal_strength = 0
nth_cycles = [20, 60, 100, 140, 180, 220]
cycle_signal_strength_list = []
j = 0

for instruction in content:
    j += 1
    if instruction == "noop":
        cycle += 1
        if cycle in nth_cycles:
            signal_strength = cycle * X
            cycle_signal_strength_list += [(cycle, X, signal_strength, j)]
    elif "addx" in instruction:
        _, n = instruction
        for i in range(2):
            cycle += 1
            if cycle in nth_cycles:
                signal_strength = cycle * X
                cycle_signal_strength_list += [
                    (cycle, X, signal_strength, instruction, j)
                ]
            if i == 1:
                X += n

print(f"part 1: {sum(i[2] for i in cycle_signal_strength_list)}")
