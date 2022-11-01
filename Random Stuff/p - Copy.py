import math

print("its loading")
file = open("primes.txt", "r")
primes = file.readlines()
for x in range(len(primes)):
    primes[x] = int(primes[x].split("\n")[0])
    i = primes[len(primes) - 1]
file.close()
print("its running")
file = open("primes.txt", "a")
while True:
    i += 1
    notprime = False
    x = 0
    while x < len(primes) and primes[x] <= math.sqrt(i):
        if i % primes[x] == 0:
            notprime = True
            x = len(primes)
        x += 1
    if notprime == False:
        primes.insert(len(primes), i)
        file.write(str(i) + "\n")
        x = len(primes)
    if i % 10000 == 0:
        file.close()
        file = open("primes.txt", "a")
