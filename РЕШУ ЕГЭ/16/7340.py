def f(n):
    if n == 1:
        return 1
    return f(n - 1) + 2**(n - 1)

print(f(12))