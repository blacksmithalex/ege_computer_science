def f(x, p):
    if x <= 12 and (p == 5 or p == 3):
        return True
    elif x > 12 and p == 5:
        return False
    elif x <= 12:
        return False
    else:
        if p % 2 == 0:
            return f(x - 12, p + 1) or f(x // 3, p + 1)
        else:
            return f(x - 12, p + 1) and f(x // 3, p + 1)

count = 0
for S in range(13, 200):
    if f(S, 1):
        count += 1
print(count)
#36 - 12 = 24