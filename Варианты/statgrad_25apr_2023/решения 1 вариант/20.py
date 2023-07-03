def f(x, y, p):
    if (x >= 48 or y >= 48) and p == 4:
        return True
    elif (x < 48 and y < 48) and p == 4:
        return False
    elif (x >= 48 or y >= 48):
        return False
    else:
        if x > y:
            if p % 2 == 1:
                return f(x + 1, y, p + 1) or f(x + 2, y, p + 1) or f(x + 3, y, p + 1) or f(x, y * 2, p + 1)
            else:
                return f(x + 1, y, p + 1) and f(x + 2, y, p + 1) and f(x + 3, y, p + 1) and f(x, y * 2, p + 1)
        elif x == y:
            if p % 2 == 1:
                return f(x + 1, y, p + 1) or f(x + 2, y, p + 1) or f(x + 3, y, p + 1) or f(x, y + 1, p + 1) or f(x, y + 2, p + 1) or f(x, y + 3, p + 1)
            else:
                return f(x + 1, y, p + 1) and f(x + 2, y, p + 1) and f(x + 3, y, p + 1) and f(x, y + 1, p + 1) and f(x, y + 2, p + 1) and f(x, y + 3, p + 1)
        else:
            if p % 2 == 1:
                return f(x, y + 1, p + 1) or f(x, y + 2, p + 1) or f(x, y + 3, p + 1) or f(x * 2, y, p + 1)
            else:
                return f(x, y + 1, p + 1) and f(x, y + 2, p + 1) and f(x, y + 3, p + 1) and f(x * 2, y, p + 1)

for S in range(1, 47 + 1):
    if f(13, S, 1):
        print(S)



