def F(n):
    if n == 0:
        return 0
    if n % 3 == 0:
        return F(n // 3)
    if n % 3 > 0:
        return n % 3 + F(n - n % 3)

for n in range(200):
    if F(n) == 9:
        print(n)