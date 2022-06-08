def f(n):
    n = str(n)
    s1 = int(n[0]) + int(n[1])
    s2 = int(n[1]) + int(n[2])
    if s1 > s2:
        return int(str(s1) + str(s2))
    else:
        return int(str(s2) + str(s1))

for n in range(100, 1000):
    if f(n) == 159:
        print(n)
