from math import sqrt
def isPrime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

pos = 1
for n in range(245690, 245756 + 1):
    if isPrime(n):
        print(pos, n)
    pos += 1