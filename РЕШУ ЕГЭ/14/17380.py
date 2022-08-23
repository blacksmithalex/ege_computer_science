def f(n):
    res = []
    while n != 0:
        res.append(n % 6)
        n //= 6
    return res[::-1]

n = 3 * 216**4 + 2 * 36**6 - 648
n = f(n)
print(n.count(5))

