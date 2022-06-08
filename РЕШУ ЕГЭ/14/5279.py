def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

for n in range(100):
    if len(f(n, 6)) == 2 and len(f(n, 5)) == 3 and f(n, 11)[-1] == 1:
        print(n)