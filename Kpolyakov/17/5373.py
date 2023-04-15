file = open('17-339.txt')
a = [int(x) for x in file]
file.close()
m19 = 100000
for x in a:
    if x % 19 == 0 and 0 < x < m19:
        m19 = x

count, sm = 0, 0
for i in range(len(a) - 1):
    if a[i] + a[i + 1] < m19:
        count += 1
        sm = max(sm, a[i] + a[i + 1])
print(count, sm)

