def F(n):
    if n == 1:
        return 1
    else:
        return F(n - 1) * (2 * n - 3)

print(F(516) / F(513))