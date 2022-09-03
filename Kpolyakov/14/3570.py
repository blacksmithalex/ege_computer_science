def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

for X in range(256, 16, -1):
    r1 = f(X, 16)[0] == 14
    r2 = f(X, 8)[1] == 5
    r3 = f(X, 4)[-1] == 1
    r4 = f(X, 2)[-3] == 1
    if r1 and r2 and r3 and r4:
        print(X)
        break
#Ответ: 237