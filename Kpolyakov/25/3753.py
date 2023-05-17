from math import sqrt
def isprime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

for p in range(3, 10000):
    if isprime(p):
        num = 2 * p**2
        if 113000000 <= num <= 114000000:
            print(num, p)