import re

# Run this python script in the same directory as the input file
filename = "input.txt"

# input
file_content = open(filename).read().strip()

# part 1
for i in range(3, len(file_content)):
    s = file_content[i : i + 4]
    if len(set(s)) == 4:
        print(i + 4)
        break

# part 2
for i in range(13, len(file_content)):
    s = file_content[i - 14 : i]
    if len(set(s)) == 14:
        print(i)
        break
