def f(x, p):
    if x >= 348 and (p == 5 or p == 3):
        return True
    elif x < 348 and p == 5:
        return False
    elif x >= 348:
        return False
    else:
        if p % 2 == 0:
            return f(x + 2, p + 1) or f(x + 4, p + 1) or f(x * 3, p + 1)
        else:
            return f(x + 2, p + 1) and f(x + 4, p + 1) and f(x * 3, p + 1)

for S in range(1, 347 + 1):
    if f(S, 1):
        print(S)

