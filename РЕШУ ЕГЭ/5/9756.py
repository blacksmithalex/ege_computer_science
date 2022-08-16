def f(n):
    n = str(n)
    p1 = int(n[0]) * int(n[1])
    p2 = int(n[1]) * int(n[2])
    if p1 < p2:
        return int(str(p1) + str(p2))
    else:
        return int(str(p2) + str(p1))

for n in range(100, 1000):
    if f(n) == 621:
        print(n)

