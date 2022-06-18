#число имеет вид n = 2p^2, p < 8000 (простое нечетное)
from math import sqrt
def isPrime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

for p in range(3, 8000):
    if isPrime(p):
        n = 2 * p**2
        if 106000000 <= n <= 107000000:
            print(n)
