def f(x, y, p):
    if x + y >= 259 and p == 3:
        return True
    elif x + y < 259 and p == 3:
        return False
    elif x + y >= 259:
        return False
    else:
        if p % 2 == 0:
            return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
        else:
            return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)

for S in range(1, 241 + 1):
    if f(17, S, 1):
        print(S)
