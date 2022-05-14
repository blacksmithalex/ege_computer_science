def f3(x, p):
    if x >= 41 and (p == 3 or p == 5 or p == 7):
        return True
    elif x < 41 and p == 7:
        return False
    elif x >= 41:
        return False
    else:
        if p % 2 == 1:
            if x * 2 <= 50:
                return f3(x + 1, p + 1) and f3(x + 2, p + 1) and f3(x * 2, p + 1)
            else:
                return f3(x + 1, p + 1) and f3(x + 2, p + 1)
        else:
            if x * 2 <= 50:
                return f3(x + 1, p + 1) or f3(x + 2, p + 1) or f3(x * 2, p + 1)
            else:
                return f3(x + 1, p + 1) or f3(x + 2, p + 1)

print('Гарантированный выигрыш первым, вторым или третим ходом у Вани')
for S in range(1, 40 + 1):
    if f3(S, 1):
        print(S)

#Ответ: 17 32