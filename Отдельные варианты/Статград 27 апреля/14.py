def f(n):
    res = []
    while n != 0:
        res.append(n % 12)
        n //= 12
    return res[::-1]

n = 15 * 1728**8 + 9 * 144**12 + 7 * 12**12 + 154
to12 = f(n)

print(to12.count(0))
#Ответ: 22