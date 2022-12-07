import pathlib
import string

filename = "input.txt"
puzzle_input = pathlib.Path(__file__).parent / filename


def process(x):
    all_groups = []
    group = []
    i = 0
    for line in input_file:
        if line.strip():
            if i < 2:
                group += [line.strip()]
                i += 1
            else:
                group += [line.strip()]
                all_groups += [group]
                group = []
                i = 0
    return all_groups


def func_2(x):
    d = {}
    v = 1
    for letter in string.ascii_letters:
        d[letter] = v
        v += 1

    t = 0
    for i in x:
        a, b, c = i[0], i[1], i[2]
        common = "".join(set(a).intersection(b).intersection(c))
        t += d[common]
    return t


if __name__ == "__main__":
    with puzzle_input.open() as input_file:
        processed_input = process(input_file)
        print(f"part 2: {func_2(processed_input)}")
