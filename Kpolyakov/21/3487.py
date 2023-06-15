def f(x, y, p):
    if x + y >= 30 and (p == 3 or p == 5):
        return True
    elif x + y < 30 and p == 5:
        return False
    elif x + y >= 30:
        return False
    else:
        if p % 2 == 0:
            return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 3, p + 1)
        else:
            return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 3, p + 1)
for S in range(1, 29 + 1):
    if 1 + S <= 29:
        if f(1, S, 1):
            print(S)

