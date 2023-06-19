file = open('17_4705.txt')
a = [int(x) for x in file]
file.close()

m3 = -10000
for x in a:
    if str(x)[-1] == '3' and x > m3:
        m3 = x

count, sm = 0, 0
for i in range(len(a) - 1):
    l1 = str(a[i])[-1] == '3' and str(a[i + 1])[-1] != '3'
    l2 = str(a[i])[-1] != '3' and str(a[i + 1])[-1] == '3'
    l3 = a[i]**2 + a[i + 1]**2 >= m3**2
    if (l1 or l2) and l3:
        count += 1
        sm = max(sm, a[i]**2 + a[i + 1]**2)
print(count, sm)