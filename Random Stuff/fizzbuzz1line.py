import time

b: list[float] = []
for j in range(100):
    start_time = time.time()
    [
        "fizzbuzz"
        if i % 3 == 0 and i % 5 == 0
        else "fizz"
        if i % 3 == 0
        else "buzz"
        if i % 5 == 0
        else i
        for i in range(1, 10001)
    ]
    b.append(time.time() - start_time)
bl: list[float] = []
for j in range(100):
    start_time = time.time()
    [
        "fizz" * int(i // 3 == (i + 2) // 3)
        + "buzz" * int(i // 5 == (i + 4) // 5)
        + str(i) * (1 - int(i // 5 == (i + 4) // 5) - int(i // 3 == (i + 2) // 3))
        for i in range(10001)
    ]
    bl.append(time.time() - start_time)

print(f"{sum(b)},{sum(b)/len(b)}\n{sum(bl)},{sum(bl)/len(bl)}")
