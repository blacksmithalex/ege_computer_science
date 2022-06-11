def f(a, b):
    if a > b or a == 15 or b == 15:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2, b)
print(f(1, 10) * f(10, 22))