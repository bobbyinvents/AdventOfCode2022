import pathlib
import string

filename = "input.txt"
puzzle_input = pathlib.Path(__file__).parent / filename


def process(x):
    l = [line.strip().split(",") for line in input_file if line.strip()]
    all_pairs = []
    for pair in l:
        new_pair = []
        for elf in pair:
            n = elf.split("-")
            for a, b in [n]:
                a, b = int(a), int(b)
                p = [*range(a, b + 1)]
            new_pair += [p]
        all_pairs += [new_pair]

    return all_pairs


def func_1(x):
    n = 0
    for pair in x:
        a, b = pair
        n += all(i in b for i in a) or all(i in a for i in b)

    return n


def func_2(x):
    n = 0
    for pair in x:
        a, b = pair
        n += any(i in b for i in a) or any(i in a for i in b)

    return n


if __name__ == "__main__":
    with puzzle_input.open() as input_file:
        processed_input = process(input_file)
        print(
            f"part 1: {func_1(processed_input)}", f"part 2: {func_2(processed_input)}"
        )
