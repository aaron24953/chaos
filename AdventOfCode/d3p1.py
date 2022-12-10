# d3p1

from d3data import data

tot = 0
data = data.split("\n")
data = [(do[0:len(do)//2], do[len(do)//2:]) for do in data]

for dat in data:
    no = True
    for da in dat[0]:
        if da in dat[1] and no:
            if da == da.lower():
                tot += ord(da) - 97 + 1
            else:
                tot += ord(da) - 65 + 26 + 1
            no = False

print(tot)
