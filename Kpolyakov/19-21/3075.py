def f19(x, p):
    if x >= 25 and p == 3:
        return True
    elif x < 25 and p == 3:
        return False
    elif x >= 25:
        return False
    else:
        if p % 2 == 1:
            return f19(x + 2, p + 1) and f19(x * 2, p + 1)
        else:
            return f19(x + 2, p + 1) or f19(x * 2, p + 1)

def f20(x, p):
    if x >= 25 and p == 4:
        return True
    elif x < 25 and p == 4:
        return False
    elif x >= 25:
        return False
    else:
        if p % 2 == 0:
            return f20(x + 2, p + 1) and f20(x * 2, p + 1)
        else:
            return f20(x + 2, p + 1) or f20(x * 2, p + 1)

def f21(x, p):
    if x >= 25 and (p == 5 or p == 3):
        return True
    elif x < 25 and p == 5:
        return False
    elif x >= 25:
        return False
    else:
        if p % 2 == 1:
            return f21(x + 2, p + 1) and f21(x * 2, p + 1)
        else:
            return f21(x + 2, p + 1) or f21(x * 2, p + 1)

print('Ответ на задачу 19')
for S in range(1, 24 + 1):
    if f19(S, 1):
        print(S)
print()

print('Ответ на задачу 20')
for S in range(1, 24 + 1):
    if f20(S, 1):
        print(S)
print()

print('Ответ на задачу 21')
for S in range(1, 24 + 1):
    if f21(S, 1):
        print(S)
