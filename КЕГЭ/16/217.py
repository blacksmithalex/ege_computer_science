def F(n):
    if n < 0:
        return -n
    elif n % 2 == 0:
        return 2 * n + 1 + F(n - 3)
    else:
        return 4 * n + 2 * F(n - 4)

print(F(33))