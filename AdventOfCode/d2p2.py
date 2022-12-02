# day 2 p2

from d2data import data

data = data.split("\n")
data = [dat.split(" ") for dat in data]
data = [(int(chr(ord(dat[0]) - 65 + 48)), int(chr(ord(dat[1]) - 88 + 48))) for dat in data]
score = 0
for dat in data:
    if dat[1] == 0:
        score += 1 + (dat[0] - 1) % 3
    elif dat[1] == 1:
        score += 3 + 1 + dat[0]
    else:
        score += 6 + 1 + (dat[0] + 1) % 3
print(score)
