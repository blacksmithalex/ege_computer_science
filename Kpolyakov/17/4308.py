def isFit(a, b, c, d):
    r1 = (a + b) % 2 == 1
    r2 = (b + c) % 2 == 1
    r3 = (c + d) % 2 == 1
    return r1 and r2 and r3

file = open('17-3.txt')
a = [int(x) for x in file]
file.close()

count, Smax = 0, 0
for i in range(len(a) - 3):
    if isFit(a[i], a[i + 1], a[i + 2], a[i + 3]):
        count += 1
        if a[i] + a[i + 1] + a[i + 2] + a[i + 3] > Smax:
            Smax = a[i] + a[i + 1] + a[i + 2] + a[i + 3]

print(count, Smax)
