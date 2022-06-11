def f(n):
    start = n
    n = bin(n)[2:]
    n = (8 - len(n)) * '0' + n
    n = n.replace('0', 'X')
    n = n.replace('1', 'Y')
    n = n.replace('X', '1')
    n = n.replace('Y', '0')
    return int(n, 2) - start

for n in range(0, 255 + 1):
    if f(n) == 133:
        print(n)








