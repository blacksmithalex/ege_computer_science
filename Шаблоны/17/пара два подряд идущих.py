file = open('17_7619.txt')
a = [int(x) for x in file]
file.close()

m2 = 0
for x in a:
    if len(str(x)) == 2 and x > m2:
        m2 = x

count, sm = 0, 0
for i in range(len(a) - 1):
    l1 = len(str(a[i])) == 2 and len(str(a[i + 1])) != 2
    l2 = len(str(a[i])) != 2 and len(str(a[i + 1])) == 2
    l3 = (a[i] + a[i + 1]) % m2 == 0
    if (l1 or l2) and l3:
        count += 1
        sm = max(a[i] + a[i + 1], sm)
print(count, sm)