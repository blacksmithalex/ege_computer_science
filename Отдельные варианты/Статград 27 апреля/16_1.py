def F(n):
    if n == 0:
        return 0
    elif n % 3 != 0:
        return F(n - 1) + 1
    else:
        return F(n // 3)


maxF = 0
for n in range(1200000000, 1600000000 + 1):
    res = F(n)
    if res > maxF:
        maxF = res
        print(maxF)

# Ответ: 37