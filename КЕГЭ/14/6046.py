def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

n = 3 * 1024**75 + 2 * 256**76 - 16**77 - 2023
r = f(n, 32)
print(r.count(0))