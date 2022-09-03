def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

a = 43 * 7**103 - 21 * 7**57 + 98
a = f(a, 7)
print(sum(a))
