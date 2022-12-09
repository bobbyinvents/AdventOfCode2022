content = [(i.split()[0],int(i.split()[-1])) for i in open("input.txt").read().strip().split("\n")]

# head starting point
hx, hy = 0, 0
# tail starting point
tx, ty = 0, 0

tail_positions = []

for motion in content:
    direction, steps = motion

    for step in range(steps):
        # move head
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
        
        # is tail adjacent to head?
        is_adjacent = abs(hx-tx) < 2 and abs(hy-ty) < 2
        
        # is tail diagonal to head?
        is_diagonal = abs(hx-tx) >= 1 and abs(hy-ty) >= 1

        if not is_adjacent:
            if direction == "R":
                # right
                tx += 1
                if is_diagonal:
                    ty = hy
            elif direction == "U":
                # up
                ty += 1
                if is_diagonal:
                    tx = hx
            elif direction == "L":
                # left
                tx -= 1
                if is_diagonal:
                    ty = hy
            elif direction == "D":
                # down
                ty -= 1
                if is_diagonal:
                    tx = hx

        tpos = (tx,ty)
        tail_positions += [tpos]

print(f"part 1: {len(set(tail_positions))}")
