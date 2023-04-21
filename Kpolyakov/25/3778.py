from math import log2, sqrt, ceil
def isprime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

bound_p = ceil(115000000**(1 / 4))
bound_two = ceil(log2(115000000))

for p in range(3, bound_p + 1):
    if isprime(p):
        for two in range(bound_two + 1):
            n = p**4 * 2**two
            if 105000000 <= n <= 115000000:
                print(n, p**4)



