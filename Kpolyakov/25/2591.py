#Решето Эратосфена
bound = 200000
primes = [True] * (bound + 1)
primes[0], primes[1] = False, False
for i in range(2, len(primes)):
    if primes[i]:
        for j in range(i ** 2, len(primes), i):
            primes[j] = False

print(primes.count(True))


