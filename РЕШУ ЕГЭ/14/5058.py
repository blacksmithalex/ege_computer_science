def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

for d in range(2, 16):
    if f(66, d)[-1] == 1 and f(40, d)[-1] == 1:
        print(d)