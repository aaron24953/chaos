# d6p2

from d6data import data
print(range(len(data)))
for i in range(len(data)):
    flag = False
    for dat in data[i:i+14]:
        if data[i:i+14].count(dat) >= 2:
            flag = True
    if not flag:
        print(i+14, data[i:i+14])
        break
