def f(x, y, p):
    if (x >= 48 or y >= 48) and p == 2:
        return True
    elif (x < 48 and y < 48) and p == 2:
        return False
    elif (x >= 48 or y >= 48):
        return False
    else:
        if x > y:
            return f(x + 1, y, p + 1) or f(x + 2, y, p + 1) or f(x + 3, y, p + 1) or f(x, y * 2, p + 1)
        elif x == y:
            return f(x + 1, y, p + 1) or f(x + 2, y, p + 1) or f(x + 3, y, p + 1) or f(x, y + 1, p + 1) or f(x, y + 2, p + 1) or f(x, y + 3, p + 1)
        else:
            return f(x, y + 1, p + 1) or f(x, y + 2, p + 1) or f(x, y + 3, p + 1) or f(x * 2, y, p + 1)

smin = 200
for x in range(1, 100):
    for y in range(1, 100):
        if f(x, y, 1):
            smin = min(smin, x + y)
print(smin)


