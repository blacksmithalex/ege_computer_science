def f(x, p):
    if x >= 50 and p == 3:
        return True
    elif x < 50 and p == 3:
        return False
    elif x >= 50:
        return False
    else:
        if p % 2 == 1:
            return f(x + 2, p + 1) and f(x * 3, p + 1)
        else:
            return f(x + 2, p + 1) or f(x * 3, p + 1)

for S in range(1, 49 + 1):
    if f(S, 1):
        print(S)
