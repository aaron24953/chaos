current = 0
for x in range(10**4,10**5+1):
    temp=(x**(1/4))//1
    if temp>current:
        current=temp
        print(x, current)