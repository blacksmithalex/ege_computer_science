def f(n):
    res = []
    while n != 0:
        res.append(n % 2)
        n //= 2
    return res[::-1]

n = 4**255 + 2**255 - 255
n = f(n)
print(n.count(1))