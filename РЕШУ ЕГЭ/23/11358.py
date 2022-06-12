def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a + 2, b) + f(a * 2, b)

print(f(3, 10) * f(10, 12))