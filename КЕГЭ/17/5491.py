file = open('17_5491.txt')
a = [int(x) for x in file]
file.close()

mi = 100000
for x in a:
    if abs(x) % 10 == 3 and x < mi:
        mi = x

count, sm = 0, 0
for i in range(len(a) - 1):
    l1 = a[i] < a[i + 1] and abs(a[i]) % 10 == 3
    l2 = a[i + 1] < a[i] and abs(a[i + 1]) % 10 == 3
    if (l1 or l2) and a[i]**2 + a[i + 1]**2 < mi**2:
        count += 1
        sm = max(sm, a[i]**2 + a[i + 1] ** 2)
print(count, sm)