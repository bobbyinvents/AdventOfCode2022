content = [
    (i.split()[0], int(i.split()[-1])) if len(i.split()) == 2 else i
    for i in open("input.txt").read().strip().split("\n")
]

cycle, X = 0, 1
row = ""
row_position = 0


def draw_pixel(cycle, X):
    sprite = [X - 1, X, X + 1]
    row_position = cycle % 40
    if row_position in sprite:
        pixel = "#"
    else:
        pixel = "."
    return pixel


def print_CRT_row(row):
    if len(row) % 40 == 0:
        print(row)
        row = ""
    return row


def debug_row():
    print(f"cycle {cycle}: {instruction}")
    print(f"Register X: {X}")
    print(row)
    print()


for instruction in content:
    if instruction == "noop":
        cycle += 1
        row += draw_pixel(cycle, X)
        row = print_CRT_row(row)

    elif "addx" in instruction:
        _, n = instruction
        for i in range(2):
            row += draw_pixel(cycle, X)
            row = print_CRT_row(row)
            # debug_row()

            cycle += 1
            if i == 1:
                X += n
