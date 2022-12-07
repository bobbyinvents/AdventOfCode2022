import pathlib
import string

filename = "input.txt"
puzzle_input = pathlib.Path(__file__).parent / filename


def process(x):
    return [
        [line.strip()[: len(line.strip()) // 2], line.strip()[len(line.strip()) // 2 :]]
        for line in input_file
        if line.strip()
    ]


def func_1(x):
    d = {}
    v = 1
    for letter in string.ascii_letters:
        d[letter] = v
        v += 1

    t = 0
    for i in x:
        a, b = i[0], i[1]
        common = "".join(set(a).intersection(b))
        t += d[common]
    return t


if __name__ == "__main__":
    with puzzle_input.open() as input_file:
        processed_input = process(input_file)
        print(f"part 1: {func_1(processed_input)}")
