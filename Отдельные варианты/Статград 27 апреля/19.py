#Гарантированный выигрыш первым ходом
def f1(x, p):
    if x >= 41 and p == 3:
        return True
    elif x < 41 and p == 3:
        return False
    elif x >= 41:
        return False
    else:
        if p % 2 == 1:
            if x * 2 <= 50:
                return f1(x + 1, p + 1) and f1(x + 2, p + 1) and f1(x * 2, p + 1)
            else:
                return f1(x + 1, p + 1) and f1(x + 2, p + 1)
        else:
            if x * 2 <= 50:
                return f1(x + 1, p + 1) or f1(x + 2, p + 1) or f1(x * 2, p + 1)
            else:
                return f1(x + 1, p + 1) or f1(x + 2, p + 1)

def f2(x, p):
    if x >= 41 and (p == 3 or p == 5):
        return True
    elif x < 41 and p == 5:
        return False
    elif x >= 41:
        return False
    else:
        if p % 2 == 1:
            if x * 2 <= 50:
                return f2(x + 1, p + 1) and f2(x + 2, p + 1) and f2(x * 2, p + 1)
            else:
                return f2(x + 1, p + 1) and f2(x + 2, p + 1)
        else:
            if x * 2 <= 50:
                return f2(x + 1, p + 1) or f2(x + 2, p + 1) or f2(x * 2, p + 1)
            else:
                return f2(x + 1, p + 1) or f2(x + 2, p + 1)
print('Гарантированный выигрыш первым ходом у Вани')
for S in range(1, 40 + 1):
    if f1(S, 1):
        print(S)
print()
print('Гарантированный выигрыш первым или вторым ходом у Вани')
for S in range(1, 40 + 1):
    if f2(S, 1):
        print(S)

#Ответ: 35