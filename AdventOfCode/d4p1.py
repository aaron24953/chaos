# d4p1

from d4data import data

data = data.split("\n")
data = [dat.split(",") for dat in data]
data = [(dat[0].split("-"), dat[1].split("-")) for dat in data]
data = [[[int(d) for d in da] for da in dat] for dat in data]

count = 0

for dat in data:
    if dat[0][0] <= dat[1][0] and dat[0][1] >= dat[1][1]:
        count += 1
    elif dat[0][0] >= dat[1][0] and dat[0][1] <= dat[1][1]:
        count += 1

print(count)
