def f(a, b):
    if a > b or a == 30 or b == 30:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2, b)

print(f(2, 16) * f(16, 33))
