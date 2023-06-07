def f(x, p):
    if x >= 55 and p == 3:
        return True
    elif x < 55 and p == 3:
        return False
    elif x >= 55:
        return False
    else:
        if p % 2 == 0:
            return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 3, p + 1)
        else:
            return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 3, p + 1)

for S in range(1, 54 + 1):
    if f(S, 1):
        print(S)