# d10p2

from d10data import data

data = [dat.split(" ") for dat in data.split("\n")]

cycle = 1
x = 1
pp = 0
pixels = ""
image = ""

for instruction in data:
    if len(instruction) == 1:
        if x <= cycle <= x+2:
            pixels += "#"
        else:
            pixels += " "
        cycle = (cycle % 40) + 1
    else:
        if x <= cycle <= x+2:
            pixels += "#"
        else:
            pixels += " "
        cycle = (cycle % 40) + 1
        if x <= cycle <= x+2:
            pixels += "#"
        else:
            pixels += " "
        cycle = (cycle % 40) + 1
        x += int(instruction[1])

for i in range(len(pixels)):
    image += pixels[i]
    if (i+1) % 40 == 0:
        image += "\n"
print(image)
