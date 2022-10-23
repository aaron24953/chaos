def getPrimes(end):
    primes = []
    for i in range(2, end + 1):
        p = True
        for j in range(2, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                p = False
                break
        if p:
            primes.append(i)
    return primes


def pFactors(num):
    primes = getPrimes(num)
    facts = []
    for i in range(len(primes)):
        while num % primes[i] == 0:
            facts.append(primes[i])
            num = num // primes[i]
    return facts
