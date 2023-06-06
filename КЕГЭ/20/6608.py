def f(x, p):
    if x <= 12 and p == 4:
        return True
    elif x > 12 and p == 4:
        return False
    elif x <= 12:
        return False
    else:
        if p % 2 == 1:
            return f(x - 12, p + 1) or f(x // 3, p + 1)
        else:
            return f(x - 12, p + 1) and f(x // 3, p + 1)

for S in range(13, 200):
    if f(S, 1):
        print(S)