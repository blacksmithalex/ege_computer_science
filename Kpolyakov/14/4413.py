def f(n):
    res = []
    while n != 0:
        res.append(n % 5)
        n //= 5
    return res[::-1]

n = (5**300 * 15**100) - (25**50 + 125**100)
n = f(n)
S = 0
for x in n:
    if x != 4:
        S += x
print(S)

