# d3p2

from d3data import data

tot = 0
data = data.split("\n")
data = [(data[i], data[i+1], data[i+2]) for i in range(0, len(data) - 1, 3)]

for dat in data:
    no = True
    for da in dat[0]:
        if da in dat[1] and da in dat[2] and no:
            if da == da.lower():
                tot += ord(da) - 97 + 1
            else:
                tot += ord(da) - 65 + 26 + 1
            no = False

print(tot)
