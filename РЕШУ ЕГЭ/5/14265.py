def f(n):
    ns = str(n)
    s1 = int(ns[0]) + int(ns[1])
    s2 = int(ns[1]) + int(ns[2])
    if s1 < s2:
        return int(str(s1) + str(s2))
    else:
        return int(str(s2) + str(s1))

for n in range(100, 1000):
    if f(n) == 812:
        print(n)

