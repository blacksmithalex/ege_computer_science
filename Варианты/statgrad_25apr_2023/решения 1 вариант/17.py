file = open('17.txt')
a = [int(x) for x in file]
mi = 10**9

for e in a:
    if len(str(e)) == 3 and str(e)[-1] == '5':
        mi = min(e, mi)

c = 0
ma = 0
for i in range(len(a) - 1):
    if ((len(str(a[i])) == 4 and len(str(a[i + 1])) != 4) or (len(str(a[i])) != 4 and len(str(a[i + 1])) == 4)):
        if (a[i]**2 + a[i + 1]**2) % mi == 0:
            c += 1
            ma = max(ma, a[i]**2 + a[i + 1]**2)

print(c, ma)