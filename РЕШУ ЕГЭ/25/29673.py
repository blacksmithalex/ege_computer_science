from math import sqrt
def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d), div.add(n // d)
    return sorted(div)

a = int(sqrt(123456789))
b = int(sqrt(223456789)) + 1

for n in range(a, b + 1):
    n = n ** 2
    div = dividers(n)
    if len(div) == 3:
        print(n, div[-1])

-----
#также верно, что число имеет виде n = p ^ 4
from math import sqrt
def isPrime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

for p in range(3, 200):
    if isPrime(p):
        n = p ** 4
        if 123456789 <= n <= 223456789:
            print(n)

