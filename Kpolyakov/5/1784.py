Задание 5:

def f(n):
    res = bin(n)[2:]
    if n % 2 == 0:
        res += '01'
    else:
        res += '10'
    return int(res, 2)

for n in range(100):
    R = f(n)
    if R > 81:
        print(R)
        break