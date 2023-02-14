def f(n):
    n = bin(n)[2:]
    n = '0' * (8 - len(n)) + n
    n = ''.join([str((int(x) + 1) % 2) for x in n])
    n = bin(int(n, 2) + 1)[2:]
    return int(n, 2)

print(f(95))