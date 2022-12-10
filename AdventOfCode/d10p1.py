# d10p1

from d10data import data

data = [dat.split(" ") for dat in data.split("\n")]

cycle = 1
x = 1
strengths = []
pp = 0

for instruction in data:
    if len(instruction) == 1:
        if cycle == 20 + pp * 40:
            pp += 1
            strengths.append(cycle * x)
        cycle+=1
    else:
        if cycle == 20 + pp * 40:
            pp += 1
            strengths.append(cycle * x)
        cycle += 1
        if cycle == 20 + pp * 40:
            pp += 1
            strengths.append(cycle * x)
        cycle += 1
        x += int(instruction[1])

print(sum(strengths))
