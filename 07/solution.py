# Run this python script in the same directory as the input file.
content = open("input.txt").read().strip().split("\n")

all_dir = []
current_dir = ""
layer = 0
parent_dir = ""
dir_list = [""]

for i in range(len(content)):
    line = content[i]

    # Linux command
    if line[0] == "$":
        # Change directory
        if "cd" in line:
            if ".." in line:
                layer -= 1
                dir_list = dir_list[:-1]
                current_dir = dir_list[-1]
                parent_dir = dir_list[-2]
            else:
                layer += 1
                parent_dir = current_dir.strip()
                current_dir = line.split("cd")[1].strip()
                dir_list += [current_dir]
            # print("cd", current_dir)
        # Print files in directory
        elif "ls" in line:
            # print("ls", current_dir)
            n = 1
            while (i + n) < len(content) and content[i + n][0] != "$":
                n += 1
            ls_output = content[i + 1 : i + n]
            # print(ls_output)

            new_dir = {"_curr": current_dir, "_layer": layer}
            total_size = 0
            for f in ls_output:
                if "dir" in f:
                    new_dir["_inner"] = new_dir.get("_inner", []) + [f.split()[1]]
                else:
                    total_size += int(f.split()[0])
            new_dir["_parent"] = parent_dir
            new_dir["_total_size"] = total_size
            all_dir += [new_dir]

# print(sorted(all_dir, key= lambda x: x["_layer"], reverse=True))

for directory in sorted(all_dir, key=lambda x: x["_layer"], reverse=True):
    directory["_total_size"] += sum(
        next(
            da["_total_size"]
            for da in all_dir
            if da["_curr"] == d
            and da.get("_parent") == directory["_curr"]
            and da["_layer"] == directory["_layer"] + 1
        )
        for d in directory.get("_inner", [])
    )

# Part 1
total_sum = 0
for d in all_dir:
    if d["_total_size"] <= 100000:
        total_sum += d["_total_size"]

print("part 1:", total_sum)

# Part 2
total_disk_space = next(d["_total_size"] for d in all_dir if d["_curr"] == "/")
disk_space_required_to_free_up_space = 30000000 - (70000000 - total_disk_space)

print(
    "part 2:",
    min(
        d["_total_size"]
        for d in all_dir
        if d["_total_size"] >= disk_space_required_to_free_up_space
    ),
)
