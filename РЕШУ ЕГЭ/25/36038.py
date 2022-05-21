def M(a):
    d = 2
    while d * d <= a:
        if a % d == 0:
            return d + (a // d)
        d += 1
    return 0

k = 0
for i in range(452021 + 1, 1000000):
    if M(i) % 7 == 3:
        k += 1
        print(i, M(i))
    if k == 5:
        break