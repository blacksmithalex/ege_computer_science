def F(n):
    if n < 3:
        return 1
    elif n % 2 == 0:
        return F(n - 1) + n
    else:
        return F(n - 2) + 2 * n

print(F(23) - F(21))