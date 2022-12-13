import math
import re
import sys

content = [i.split("\n") for i in open("test.txt").read().strip().split("\n\n")]
monkeys = []

for monkey in content:
    monkey_dict = {}
    throw_targets = []
    for i in range(len(monkey)):
        line = monkey[i]
        if i == 1:
            monkey_dict["starting_items"] = [*map(int, re.findall("\d+", line))]
        if i == 2:
            monkey_dict["operation"] = line.split()[-3:]
        if i == 3:
            monkey_dict["test"] = [int(line.split()[-1])]
        if i == 4:
            throw_targets += [line.split()[-1]]
        if i == 5:
            throw_targets += [line.split()[-1]]
            throw_targets = [*map(int, throw_targets)]
            monkey_dict["test"] += [throw_targets]

    monkeys += [monkey_dict]


round_n = 10_000
inspections = [0 for _ in range(len(monkeys))]
lcm = next(
    i for i in range(1, sys.maxsize) if all(i % m["test"][0] == 0 for m in monkeys)
)

for _ in range(round_n):
    n = 0
    for m in range(len(monkeys)):
        monkey = monkeys[m]
        starting_items = monkey["starting_items"]
        op, op2 = monkey["operation"][1:]
        test = monkey["test"][0]
        test_true, test_false = monkey["test"][1]

        for i in range(len(starting_items)):
            item = starting_items[i]
            op3 = [item, op2][op2 != "old"]

            # worry level increased by monkey
            worry_level = eval(f"{item} {op} {op3}")

            # pass item
            if worry_level % test == 0:
                # store the mod of the lowest common multiple
                monkeys[test_true]["starting_items"] += [worry_level % lcm]
            else:
                monkeys[test_false]["starting_items"] += [worry_level % lcm]

        inspections[m] += len(starting_items)

        # remove all items
        monkey["starting_items"] = []

print(f"part 2: {math.prod(sorted(inspections)[-2:])}")
