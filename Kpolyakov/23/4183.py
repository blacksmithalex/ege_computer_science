def f(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a, b + 8) + f(a, b * 2) + f(a, b * 2 + 1)

print(f(102, 43) * f(43, 5))