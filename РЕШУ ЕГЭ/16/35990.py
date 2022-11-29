def F(n):
    if n == 0:
        return 0
    if n % 2 == 0 and n > 0:
        return F(n // 2)
    if n % 2 != 0:
        return 1 + F(n - 1)

count = 0
for n in range(1, 500 + 1):
    if F(n) == 3:
        count += 1
print(count)
