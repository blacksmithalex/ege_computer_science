def f(n):
    n = bin(n)[2:][::-1]
    if n.count('0') == 0:
        return -1
    else:
        n = n.replace('0', n[-2:], 1)
        return int(n, 2)

for n in range(2, 500):
    R = f(n)
    if R == 119:
        print(n)


