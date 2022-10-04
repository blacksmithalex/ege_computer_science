file = open('17.txt')
a = [int(x) for x in file]
file.close()

M3 = 0
for x in a:
    if str(x)[-1] == '3' and x > M3:
        M3 = x

count, M = 0, 0
for i in range(len(a) - 1):
    l1 = str(a[i])[-1] == '3' and str(a[i + 1])[-1] != '3'
    l2 = str(a[i])[-1] != '3' and str(a[i + 1])[-1] == '3'
    if l1 or l2:
        if a[i] ** 2 + a[i + 1] ** 2 >= M3 ** 2:
            count += 1
            if a[i] ** 2 + a[i + 1] ** 2 > M:
                M = a[i] ** 2 + a[i + 1] ** 2
print(count, M)

