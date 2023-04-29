from math import sqrt
def isprime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

res = []
for p in range(3, 100):
    if isprime(p):
        for k in range(30):
            x = p**4 * 2**k
            if 55000000 <= x <= 60000000:
                res.append([x, p**4])
for var in sorted(res):
    print(*var)
