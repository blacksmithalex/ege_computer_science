def f(a, b):
    if a > b or a == 17 or b == 17:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2, b)

print(f(1, 10) * f(10, 21))