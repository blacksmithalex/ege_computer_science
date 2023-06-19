file = open('17_8504.txt')
a = [int(x) for x in file]
file.close()

m5 = 100000
for x in a:
    if len(str(x)) == 3 and x % 10 == 5 and x < m5:
        m5 = x

count, sm = 0, 0
for i in range(len(a) - 1):
    l1 = len(str(a[i])) == 3 or len(str(a[i + 1])) == 3
    l2 = (a[i] + a[i + 1]) % m5 == 0
    if l1 and l2:
        count += 1
        sm = max(sm, a[i] + a[i + 1])

print(count, sm)