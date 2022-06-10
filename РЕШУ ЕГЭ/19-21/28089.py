def f(x, p):
    if x > 53 and p == 3:
        return True
    if x <= 53 and p == 3:
        return False
    else:
        return f(x + 1, p + 1) or f(x * 2, p + 1)
for S in range(1, 53 + 1):
    if f(S, 1) == True:
        print(S)
        break