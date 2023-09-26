file = open('17_6605.txt')
a = [int(x) for x in file]
file.close()

m5 = -10000
for x in a:
    if abs(x) % 10 == 5 and x > m5:
        m5 = x

count, sm = 0, 0
for i in range(len(a) - 1):
    l1 = abs(a[i]) % 10 == 5 and abs(a[i + 1]) % 10 != 5
    l2 = abs(a[i]) % 10 != 5 and abs(a[i + 1]) % 10 == 5
    l3 = abs(a[i]**2 - a[i + 1]**2) <= m5**2
    if (l1 or l2) and l3:
        count += 1
        sm = max(sm, abs(a[i]**2 - a[i + 1]**2))
print(count, sm)
