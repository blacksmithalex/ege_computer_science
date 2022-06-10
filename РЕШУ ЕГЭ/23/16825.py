def f(a, b):
    if a > b or a == 12 or b == 12 or a == 6 or b == 6:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a * 2, b) + f(a + 3, b)

print(f(3, 16))
