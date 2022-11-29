def f19(x, y, p):
    if x + y <= 20 and p == 3:
        return True
    elif x + y > 20 and p == 3:
        return False
    elif x + y <= 20:
        return False
    else:
        return f19(x - 1, y , p + 1) or f19(x, y - 1, p + 1) or \
               f19(x // 2 + x % 2, y, p + 1) or f19(x, y // 2 + y % 2, p + 1)
    #x//2 + x % 2 необходимо, чтобы в случае нечетного значения округление происходило наверх

for S in range(100, 20, -1):
    if f19(10, S, 1):
        print(S)
        break

