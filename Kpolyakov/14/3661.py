def f(n, d):
    res = []
    while n != 0:
        res.append(n % d)
        n //= d
    return res[::-1]

for d in range(2, 10 + 1):
    print(d, f(432, d))
#6 [2, 0, 0, 0]
#8 [6, 6, 0]
#9 [5, 3, 0]
#10 [4, 3, 2]
#Ответ: 33