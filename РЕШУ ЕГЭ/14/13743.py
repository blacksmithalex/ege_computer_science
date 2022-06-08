def f(n):
    res = []
    while n != 0:
        res.append(n % 7)
        n = n // 7
    return res[::-1]

a = 49**10 + 7**30 - 49
R = f(a)
print(R.count(6))