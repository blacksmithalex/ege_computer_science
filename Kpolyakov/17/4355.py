def isFit(a, b, c):
    res = [a % 16 == 0, b % 16 == 0, c % 16 == 0]
    return res.count(True) >= 2

count, Smax = 0, 0
file = open('test.txt')
a = [int(x) for x in file]
file.close()

for i in range(len(a) - 2):
    if isFit(a[i], a[i + 1], a[i + 2]):
        count += 1
        Smax += max(a[i], a[i + 1], a[i + 2])
print(count, Smax)