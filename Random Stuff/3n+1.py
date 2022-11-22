steps = 0
maxSteps = 0
# 2**1000000-1 13420758
start = 2**68 + 1
end = 2**69
if start % 2 != 1:
    print("must be odd")
for i in range(start, end + 1, 2):
    num = start
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        steps += 1
        if steps % 10000 == 0:
            print(steps // 1000, "k")
    if steps > maxSteps:
        maxSteps = steps
        print(i, steps)
