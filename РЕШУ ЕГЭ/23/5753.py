def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    else:
        return f(a + 1, b) + f(a + 5, b)

print(f(2, 15))
