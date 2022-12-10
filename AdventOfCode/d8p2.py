# d8p2

from d8data import data

data = [[int(letter) for letter in line] for line in data.split("\n")]
visibility = [[0 for i in range(len(data[0]))] for j in range(len(data))]

for i in range(len(data)-1):
    for j in range(len(data[0])-1):
        height = data[i][j]
        if not height or i == 0 or j == 0:
            visibility[i][j] = 0
        else:
            east = 0
            for k in range(1, len(data[0]) - j):
                if data[i][j+k]<height:
                    east+=1
                else:
                    east+=1
                    break
            weast = 0
            for k in range(j-1, -1, -1):
                if data[i][k]<height:
                    weast+=1
                else:
                    weast+=1
                    break
            seast = 0
            for k in range(1, len(data[0]) - i):
                if data[i+k][j]<height:
                    seast+=1
                else:
                    seast+=1
                    break
            neast = 0
            for k in range(i-1, -1, -1):
                if data[k][j]<height:
                    neast+=1
                else:
                    neast+=1
                    break
            visibility[i][j] = east * weast * neast * seast

print(visibility,max([max(arr) for arr in visibility]))
