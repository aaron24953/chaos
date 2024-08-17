# an optimiser for the base feature of spaceidle


def value_base(base: list[list[int]]):
    value = 0
    for i in range(len(base)):
        for j in range(len(base[i])):
            if base[i][j] == 0:
                boosters = 0
                if i != 0:
                    if base[i - 1][j] == 1:
                        boosters += 1
                if i != len(base) - 1:
                    if base[i + 1][j] == 1:
                        boosters += 1
                if j != 0:
                    if base[i][j - 1] == 1:
                        boosters += 1
                if j != len(base[i]) - 1:
                    if base[i][j + 1] == 1:
                        boosters += 1
                value += BOOTSTER_MULTIPLIER**boosters
    return value


def output_base(base: list[list[int]]):
    output = ""
    for row in base:
        for space in row:
            if space == 0:
                output += "G"
            elif space == 1:
                output += "B"
            else:
                output += " "
        output += "\n"
    print(output)


# base has -1 for squares that cannot be filled, 0 for generators and 1 for boosters
base = [
    [0, 0, -1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, -1],
]
BOOTSTER_MULTIPLIER = 1.73205

spaces = sum([row.count(0) for row in base])
# print(spaces)
maximum_value = 0
for i in range(2**spaces):
    permutation = bin(i)[2:]
    permutation = "0" * (spaces - len(permutation)) + permutation
    # print((permutation))
    index = 0
    for j in range(len(base)):
        for k in range(len(base[j])):
            if base[j][k] != -1:
                base[j][k] = int(permutation[index])
                index += 1
    value = value_base(base)
    if value > maximum_value:
        maximum_value = value
        print(maximum_value)
        output_base(base)
print("complete")
