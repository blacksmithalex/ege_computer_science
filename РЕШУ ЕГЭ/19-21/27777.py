def f(x, y, p):
    if x + y <= 40 and p == 3:
        return True
    if x + y > 40 and p == 3:
        return False
    if x + y <= 40:
        return False
    else:
        return f(x - 1, y, p + 1) or f(x // 2 + x % 2, y, p + 1) or f(x, y - 1, p + 1) or f(x, y // 2 + y % 2, p + 1)

for S in range(100, 20, -1):
    if f(20, S, 1) == True:
        print(S)
        break