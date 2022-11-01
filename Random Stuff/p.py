import math

print("its loading")
file = open("primes.txt", "r")
endScan = False
highestP = 0
while endScan == False:
    try:
        temp = int(file.readline())
        highestP = temp
    except:
        endScan = True
        file.close()
        print("highest prime so far:", highestP)
file = open("primes.txt", "r")
target = math.sqrt(highestP) * 2
currentP = 0
primes = []
while currentP < target:
    temp = int(file.readline())
    primes.insert(len(primes), temp)
    currentP = temp
file.close()
print("its running")
file = open("primes.txt", "a")
i = highestP
while True:
    i += 1
    notPrime = False
    x = 0
    rootI = math.sqrt(i)
    while primes[x] <= rootI and notPrime == False:
        if i % primes[x] == 0:
            notPrime = True
        x += 1
    if notPrime == False:
        file.write(str(i) + "\n")
    if i % 10000 == 0:
        file.close()
        file = open("primes.txt", "a")
