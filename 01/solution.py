import pathlib

puzzle_input = pathlib.Path(__file__).parent / "input.txt"

def process(x):
    a = 0
    t = []
    for line in input_file:
        if line == "\n":
            t += [a]
            a = 0
        else:
            a += int(line)
    t += [a]
    return t


def func_1(x):
    return max(x)


def func_2(x):
    return sum(sorted(x)[-3:])


if __name__ == "__main__":
    with puzzle_input.open() as input_file:
        processed_input = process(input_file)
        print(f"part 1: {func_1(processed_input)}")
        print(f"part 2: {func_2(processed_input)}")
