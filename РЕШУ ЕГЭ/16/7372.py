def F(n):
    if n == 1:
        return 1
    return F(n - 1) * n

print(F(6))