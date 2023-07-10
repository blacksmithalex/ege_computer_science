def F(n):
    if n == 0 or n == 1:
        return 1
    else:
        return 3 * F(n - 1) - F(n - 2)

print(F(6))