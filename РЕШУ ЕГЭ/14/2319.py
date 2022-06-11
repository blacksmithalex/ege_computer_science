def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

for d in range(5, 1000):
    if f(31, d)[-1] == 4:
        print(d, end = ' ')
