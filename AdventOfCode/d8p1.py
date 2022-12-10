# d8p1

from d8data import data

data = [[int(letter) for letter in line] for line in data.split("\n")]
visible = [[0 for i in range(len(data[0]))] for j in range(len(data))]

for i in range(len(data)):
    biggest = -1
    for j in range(len(data[0])):
        if biggest<data[i][j]:
            visible[i][j] = 1
            biggest = data[i][j]

    biggest = -1
    for j in range(len(data[0])-1, -1, -1):
        if biggest<data[i][j]:
            visible[i][j] = 1
            biggest = data[i][j]

for i in range(len(data[0])):
    biggest = -1
    for j in range(len(data)):
        if biggest<data[j][i]:
            visible[j][i] = 1
            biggest = data[j][i]

    biggest = -1
    for j in range(len(data)-1, -1, -1):
        if biggest<data[j][i]:
            visible[j][i] = 1
            biggest = data[j][i]

print(sum([arr.count(1) for arr in visible]))
