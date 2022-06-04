def f(n):
    b = bin(n)[2:][1:]
    b = int(b, 2)
    return n - b

alls = set()
for n in range(10, 1000 + 1):
    alls.add(f(n))

print(len(alls))