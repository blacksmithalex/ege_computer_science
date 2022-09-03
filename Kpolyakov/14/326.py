def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

for d in range(2, 10 + 1):
    print(d, f(30, d))

#Ответ: 4