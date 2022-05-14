#Гарантированный выигрыш первым ходом
def f4(x, p):
    if x >= 41 and p == 2:
        return True
    elif x < 41 and p == 2:
        return False
    elif x >= 41:
        return False
    else:
        if p % 2 == 0:
            if x * 2 <= 50:
                return f4(x + 1, p + 1) and f4(x + 2, p + 1) and f4(x * 2, p + 1)
            else:
                return f4(x + 1, p + 1) and f4(x + 2, p + 1)
        else:
            if x * 2 <= 50:
                return f4(x + 1, p + 1) or f4(x + 2, p + 1) or f4(x * 2, p + 1)
            else:
                return f4(x + 1, p + 1) or f4(x + 2, p + 1)

def f5(x, p):
    if x >= 41 and (p == 2 or p == 4):
        return True
    elif x < 41 and p == 4:
        return False
    elif x >= 41:
        return False
    else:
        if p % 2 == 0:
            if x * 2 <= 50:
                return f5(x + 1, p + 1) and f5(x + 2, p + 1) and f5(x * 2, p + 1)
            else:
                return f5(x + 1, p + 1) and f5(x + 2, p + 1)
        else:
            if x * 2 <= 50:
                return f5(x + 1, p + 1) or f5(x + 2, p + 1) or f5(x * 2, p + 1)
            else:
                return f5(x + 1, p + 1) or f5(x + 2, p + 1)
print('Гарантированный выигрыш первым ходом у Пети')
for S in range(1, 40 + 1):
    if f4(S, 1):
        print(S)
print()
print('Гарантированный выигрыш первым или вторым ходом у Пети')
for S in range(1, 40 + 1):
    if f5(S, 1):
        print(S)

#Кандидаты: 10 18 19 36 37
#Ответ: 19