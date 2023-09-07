def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

n = 16**820 - 2**761 + 14
n4 = f(n, 4)
print(n4.count(0))