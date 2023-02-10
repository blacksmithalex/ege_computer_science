def f(n):
    n = bin(n)[3:]
    if n.count('1') % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '0'
    return int(n, 2)

alls = set()
for n in range(1, 100000):
    if f(n) < 450:
        alls.add(f(n))
print(max(alls))
