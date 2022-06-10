def f19(x, y, p):
    if x + y >= 91 and p == 3:
        return True
    elif x + y < 91 and p == 3:
        return False
    else:
        return f19(x + 1, y, p + 1) or f19(x, y + 1, p + 1) or f19(x * 4, y, p + 1) or f19(x, y * 4, p + 1)

print('Ответ для задачи 19:')
for S in range(1, 85 + 1):
    if f19(5, S, 1) == True:
        print(S)
        break
print()

def f20(x, y, p):
    if x + y >= 91 and p == 4:
        return True
    elif x + y < 91 and p == 4:
        return False
    elif x + y >= 91:
        return False
    else:
        if p % 2 == 1:
            return f20(x + 1, y, p + 1) or f20(x, y + 1, p + 1) or f20(x * 4, y, p + 1) or f20(x, y * 4, p + 1)
        else:
            return f20(x + 1, y, p + 1) and f20(x, y + 1, p + 1) and f20(x * 4, y, p + 1) and f20(x, y * 4, p + 1)

print('Ответ для задачи 20:')
for S in range(1, 85 + 1):
    if f20(5, S, 1) == True:
        print(S)
print()

def f21(x, y, p):
    if x + y >= 91 and (p == 5 or p == 3):
        return True
    elif x + y < 91 and p == 5:
        return False
    elif x + y >= 91:
        return False
    else:
        if p % 2 == 0:
            return f21(x + 1, y, p + 1) or f21(x, y + 1, p + 1) or f21(x * 4, y, p + 1) or f21(x, y * 4, p + 1)
        else:
            return f21(x + 1, y, p + 1) and f21(x, y + 1, p + 1) and f21(x * 4, y, p + 1) and f21(x, y * 4, p + 1)

print('Ответ для задачи 21:')
for S in range(1, 85 + 1):
    if f21(5, S, 1) == True:
        print(S, end = ' ')
print()