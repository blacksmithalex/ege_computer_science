file = open('17.txt')
a = [int(x) for x in file]
file.close()

count, s = 0, 0
for x in a:
    if x % 2 == 1:
        s += x
        count += 1
avg = s / count

count, M = 0, 0
for i in range(len(a) - 1):
    if (a[i] % 5 == 0 or a[i + 1] % 5 == 0) and (a[i] < avg or a[i + 1] < avg):
        count += 1
        if a[i] + a[i + 1] > M:
            M = a[i] + a[i + 1]
print(count, M)