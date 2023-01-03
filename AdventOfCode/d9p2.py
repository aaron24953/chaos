# d9p2

from d9data import data

data = [(dat.split(" ")[0], int(dat.split(" ")[1])) for dat in data.split("\n")]

rope = [[0,0] for i in range(10)]
grid = [[0 for i in range(500)] for j in range(500)]

for line in data:
    for i in range(line[1]):
        for j in range(1, len(rope)):
            if j == 1:
                if line[0] == "U":
                    rope[j-1][1] += 1
                elif line[0] == "D":
                    rope[j-1][1] -= 1
                elif line[0] == "L":
                    rope[j-1][0] += 1
                elif line[0] == "R":
                    rope[j-1][0] -= 1
                else:
                    print("oh no")
            movedv = False
            movedh = False
            if rope[j-1][0] > rope[j][0] + 1:
                rope[j][0] += 1
                movedh = True
            elif rope[j-1][0] < rope[j][0] - 1:
                rope[j][0] -= 1
                movedh = True
            if rope[j-1][1] > rope[j][1] + 1:
                rope[j][1] += 1
                movedv = True
            elif rope[j-1][1] < rope[j][1] -1:
                rope[j][1] -=1
                movedv = True
            if movedv and not movedh:
                if rope[j-1][0] > rope[j][0]:
                    rope[j][0] += 1
                elif rope[j-1][0] < rope[j][0]:
                    rope[j][0] -=1
            if movedh and not movedv:
                if rope[j-1][1] > rope[j][1]:
                    rope[j][1] += 1
                elif rope[j-1][1] < rope[j][1]:
                    rope[j][1] -=1
            if j == len(rope) - 1:
                grid[rope[j][0]][rope[j][1]] = 1

print(sum([sum(arr) for arr in grid]))
