# day 2 p1

from d2data import data

data = data.split("\n")
data = [dat.split(" ") for dat in data]
data = [(int(chr(ord(dat[0]) - 65 + 48)), int(chr(ord(dat[1]) - 88 + 48))) for dat in data]
score = 0
for dat in data:
    if (dat[0] + 1) % 3 == dat[1]:  # win
        score += 6
    elif dat[0] == dat[1]:
        score += 3
    score += dat[1] + 1
print(score)
