file = open('test.txt')
n = int(file.readline())
d = {}
for _ in range(n):
    a, b = [int(x) for x in file.readline().split()]
    d[a] = sorted(d.get(a, []) + [b])
file.close()

for r in sorted(d, reverse = True):
    a = d[r]
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] == 14:
            print(r, a[i] + 1)
            quit()