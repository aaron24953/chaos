# d6p1

from d6data import data
for i in range(len(data)):
    flag = False
    for dat in data[i:i+4]:
        if data[i:i+4].count(dat) >= 2:
            flag = True
    if not flag:
        print(i+4, data[i:i+4])
        break
