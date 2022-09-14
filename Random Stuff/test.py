# type: ignore
import random
x = [i for i in range(1,13)]
o=[]
for i in range(len(x)):
    p = random.choice(x)
    x.remove(p)
    o.append(p)
print(o)
