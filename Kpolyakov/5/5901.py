def f(n):
    n -= bin(n)[2:].count('0')
    n = bin(n)[2:]
    n = n[-3:] + n
    return int(n, 2)

for n in range(8, 100):
    if f(n) > 224:
        print(n, f(n))
        break




