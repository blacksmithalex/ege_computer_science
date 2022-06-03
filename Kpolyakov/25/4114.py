from math import sqrt
def f(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

primes = [x for x in range(3, 1000000 + 1) if f(x) == True]

for i in range(len(primes) - 1):
    dist = primes[i + 1] - primes[i] - 1
    if dist >= 90:
        print(primes[i], primes[i + 1])

