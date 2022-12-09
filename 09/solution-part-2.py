content = [
    (i.split()[0], int(i.split()[-1]))
    for i in open("input.txt").read().strip().split("\n")
]

# all knots starting point
knots = [[0, 0] for i in range(10)]

tail_positions = []

for motion in content:
    direction, steps = motion

    for step in range(steps):
        # move head
        hx, hy = knots[0]
        if direction == "R":
            # right
            hx += 1
        elif direction == "U":
            # up
            hy += 1
        elif direction == "L":
            # left
            hx -= 1
        elif direction == "D":
            # down
            hy -= 1
        knots[0] = hx, hy

        for i in range(1, len(knots)):
            tx, ty = knots[i]
            hx, hy = knots[i - 1]

            # check the direction of the preceding knot's movement for each individual knot
            dx, dy = hx - tx, hy - ty
            if (dx, dy) == (2, 0):
                # right
                tx += 1
            elif (dx, dy) == (0, 2):
                # up
                ty += 1
            elif (dx, dy) == (-2, 0):
                # left
                tx -= 1
            elif (dx, dy) == (0, -2):
                # down
                ty -= 1
            elif (dx, dy) in [(2, -2), (2, -1), (1, -2)]:
                # diagonal down right
                tx += 1
                ty -= 1
            elif (dx, dy) in [(2, 2), (1, 2), (2, 1)]:
                # diagonal up right
                tx += 1
                ty += 1
            elif (dx, dy) in [(-2, 2), (-1, 2), (-2, 1)]:
                # diagonal up left
                tx -= 1
                ty += 1
            elif (dx, dy) in [(-2, -2), (-2, -1), (-1, -2)]:
                # diagonal down right
                tx -= 1
                ty -= 1
            knots[i] = tx, ty

        tpos = (knots[-1][0], knots[-1][1])
        tail_positions += [tpos]

print(f"part 2: {len(set(tail_positions))}")
