file = open('27_B.txt')
n = int(file.readline())

Smax, dmin = 0, 20000
for _ in range(n):
    a, b, c = sorted([int(x) for x in file.readline().split()])
    Smax += c
    if (c - b) % 109 != 0 and c - b < dmin:
        dmin = c - b
    elif (c - a) % 109 != 0 and c - a < dmin:
        dmin = c - a

if Smax % 109 != 0:
    print(Smax)
else:
    print(Smax - dmin)