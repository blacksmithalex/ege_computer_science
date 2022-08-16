def f(n):
    res = []
    while n != 0:
        res.append(n % 9)
        n //= 9
    return res[::-1]

n = 729**8 - 3**18 + 85
n = f(n)
print(n.count(0))
