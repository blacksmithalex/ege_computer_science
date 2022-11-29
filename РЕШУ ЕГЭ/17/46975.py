file = open('17-2.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

S2, count2 = 0, 0
for x in a:
    if x % 2 == 0:
        S2 += x
        count2 += 1
avg2 = S2 / count2

count, M = 0, 0
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 and a[i + 1] < avg2) or (a[i] < avg2 and a[i + 1] % 3 == 0):
        count += 1
        if a[i] + a[i + 1] > M:
            M = a[i] + a[i + 1]
print(count, M)

