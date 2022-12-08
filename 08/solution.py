import math

content = open("input.txt").read().strip().split("\n")

visible_trees = 0
scenic_scores = []
for i, row in enumerate(content):
    for j, curr_tree in enumerate(row):
        # Part 2
        north = [content[a][j] < curr_tree for a in range(i - 1, -1, -1)]
        south = [content[a][j] < curr_tree for a in range(i + 1, len(content))]
        east = [row[a] < curr_tree for a in range(j + 1, len(row))]
        west = [row[a] < curr_tree for a in range(j - 1, -1, -1)]

        # Part 1
        if all(north) or all(south) or all(east) or all(west):
            visible_trees += 1

        # Part 2
        def f(x):
            a = 0
            for i, v in enumerate(x):
                a = i + 1
                if not v:
                    a = i + 1
                    break
            return a

        scenic_scores += [math.prod(map(lambda x: f(x), [north, south, east, west]))]

print(f"part 1: {visible_trees}")
print(f"part 2: {max(scenic_scores)}")
