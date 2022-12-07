import pathlib

filename = "input.txt"
puzzle_input = pathlib.Path(__file__).parent / filename


def process(x):
    return [[line.strip()[0], line.strip()[2]] for line in input_file if line.strip()]


def func_1(x):
    d1 = {"A": "Y", "B": "Z", "C": "X"}
    d2 = {"X": 1, "Y": 2, "Z": 3}
    d3 = {"A": "X", "B": "Y", "C": "Z"}
    total = 0
    for i in x:
        t = 0
        a, b = i[0], i[1]
        if d3[a] == b:
            t += 3
        elif b == d1[a]:
            t += 6

        t += d2[b]
        total += t
    return total


def func_2(x):
    d1_win = {"A": "Y", "B": "Z", "C": "X"}
    d1_points = {"A": 1, "B": 2, "C": 3}
    d2 = {"X": 1, "Y": 2, "Z": 3}
    d3_draw = {"A": "X", "B": "Y", "C": "Z"}
    d4_lose = {"A": "Z", "B": "X", "C": "Y"}
    total = 0
    for i in x:
        t = 0
        a, b = i[0], i[1]
        if b == "X":
            t += 0
            t += d2[d4_lose[a]]
        elif b == "Y":
            t += 3
            t += d1_points[a]
        elif b == "Z":
            t += 6
            t += d2[d1_win[a]]
        total += t
    return total


if __name__ == "__main__":
    with puzzle_input.open() as input_file:
        processed_input = process(input_file)
        print(
            f"part 1: {func_1(processed_input)}", f"part 2: {func_2(processed_input)}"
        )
