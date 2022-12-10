# d9p1

from d9data import data

data = [(dat.split(" ")[0], int(dat.split(" ")[1])) for dat in data.split("\n")]

head = [0,0]
tail = [0,0]
grid = [[0 for i in range(500)] for j in range(500)]

for line in data:
    for i in range(line[1]):
        movedv = False
        movedh = False
        if line[0] == "U":
            head[1] += 1
        elif line[0] == "D":
            head[1] -= 1
        elif line[0] == "L":
            head[0] += 1
        elif line[0] == "R":
            head[0] -= 1
        else:
            print("oh no")
        if head[0] > tail[0] + 1:
            tail[0] += 1
            movedh = True
        elif head[0] < tail[0] - 1:
            tail[0] -= 1
            movedh = True
        if head[1] > tail[1] + 1:
            tail[1] += 1
            movedv = True
        elif head[1] < tail[1] -1:
            tail[1] -=1
            movedv = True
        if movedv and not movedh:
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -=1
        if movedh and not movedv:
            if head[1] > tail[1]:
                tail[1] += 1
            elif head[1] < tail[1]:
                tail[1] -=1

        grid[tail[0]][tail[1]] = 1

print(sum([sum(arr) for arr in grid]))
