file = open('107_17.txt')
a = [int(x) for x in file]
file.close()

m21 = 100000
for x in a:
    if x % 21 == 0 and x < m21:
        m21 = x

count, ms = 0, 0
for i in range(len(a) - 1):
    if a[i] % m21 == 0 or a[i + 1] % m21 == 0:
        count += 1
        s = a[i] + a[i + 1]
        if s > ms:
            ms = s
print(count, ms)


