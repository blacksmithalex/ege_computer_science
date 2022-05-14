def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(int(str(a) + '1'), b)

print(f(1, 333))

#Ответ: 73