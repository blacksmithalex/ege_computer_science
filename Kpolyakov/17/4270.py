file = open('17-1.txt')
a = [int(x) for x in file]
file.close()

count, m = 0, 10000
for i in range(len(a) - 1):
    l1 = abs(a[i]) % 10 == 6 and a[i] % 3 == 0
    l2 = abs(a[i + 1]) % 10 == 6 and a[i + 1] % 3 == 0
    if l1 or l2:
        count += 1
        m = min(m, a[i], a[i + 1])
print(count, m)

