from math import sqrt
def isprime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True
p = []
n = 2
while len(p) != 7:
    if isprime(n):
        p.append(n)
    n += 1

r = p[0]**4 * p[1]**4 * p[2]**2 * p[3] * p[4] * p[5] * p[6]
print(r, p[-1])
