def f(x, p):
    if x >= 43 and p == 4:
        return True
    elif x < 43 and p == 4:
        return False
    elif x >= 43:
        return False
    else:
        if p % 2 == 1:
            return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 3, p + 1)
        else:
            return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 3, p + 1)

for S in range(1, 42 + 1):
    if f(S, 1):
        print(S)
        
