def to4(n):
    res = ''
    while n != 0:
        res += str(n % 4)
        n //= 4
    return res[::-1]

def oper1(n):
    return to4(int(n, 4) + 2)

def oper2(n):
    return to4(int(n, 4) + 3)

def f(a, b):
    if int(a) > int(b):
        return 0
    elif a == b:
        return 1
    else:
        return f(oper1(a), b) + f(oper2(a), b) + f(a + '0', b)

print(f(to4(1), to4(16)))




