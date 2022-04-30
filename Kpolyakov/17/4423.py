def isFit(a, b, c):
    r1 = a > 0 and a % 10 == 9
    r2 = b > 0 and b % 10 == 9
    r3 = c > 0 and c % 10 == 9
    return (not r1) and r2 and (not r3)

file = open('17-204.txt')
a = [int(x) for x in file]
file.close()

count = 0
maxS = 0
for i in range(1, len(a) - 1):
    if isFit(a[i - 1], a[i], a[i + 1]):
        count += 1
        if a[i - 1] + a[i] + a[i + 1] > maxS:
            maxS = a[i - 1] + a[i] + a[i + 1]
print(count, maxS)