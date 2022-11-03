import time

numI = 1
numP = 100
b: list[float] = []
for j in range(numI):
    start_time = time.time()
    [
        "fizzbuzz"
        if i % 3 == 0 and i % 5 == 0
        else "fizz"
        if i % 3 == 0
        else "buzz"
        if i % 5 == 0
        else i
        for i in range(1, numP+1)
    ]
    b.append(time.time() - start_time)
bl: list[float] = []
for j in range(numI):
    start_time = time.time()
    p=[
        "fizz" * (1+i // 3 - (i + 2) // 3)
        + "buzz" * (1+i // 5 - (i + 4) // 5)
        + str(i) * (1 - (1 + i // 5 - (i + 4) // 5) - (1+i // 3 - (i + 2) // 3))
        for i in range(1, numP+1)
    ]
    print(p)
    bl.append(time.time() - start_time)

print(f"{sum(b)},{sum(b)/len(b)}\n{sum(bl)},{sum(bl)/len(bl)}")
