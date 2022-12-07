import re

# Run this python script in the same directory as your input file
filename = "input.txt"
if filename == "test.txt":
    n = 3
elif filename == "input.txt":
    n = 8

# input
file_content = open(filename).read().strip().split("\n")

# crate stacks
file_content_nostrip = open(filename).read().split("\n")
stack_indexes = [file_content[n].index(i) for i in file_content[n] if i.strip()]

stacks = []
for i in stack_indexes:
    stack = []
    for j in range(n - 1, -1, -1):
        # print(j, i)
        crate = file_content_nostrip[j][i]
        if crate.strip():
            stack += [crate]
    stacks += [stack]
# print(f"stacks: {stacks}")

# instructions
RE_INT = re.compile(r"^[-+]?([1-9]\d*|0)$")
instructions = [[*map(int, re.findall("[0-9.]+", i))] for i in file_content[n + 2 :]]
# print(f"instructions: {instructions}")


for i in instructions:
    move, s1, s2 = i[0], i[1] - 1, i[2] - 1

    # part 1
    stack = stacks[s1][-move:][::-1]
    # part 2: Uncomment below for the solution to part 2
    # stack = stacks[s1][-move:]

    stacks[s1] = stacks[s1][:-move]
    stacks[s2] += stack
    # print(move, s1, s2, stack)

print("".join(i[-1] for i in stacks))
