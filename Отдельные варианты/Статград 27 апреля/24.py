file = open('24.txt')
a = file.readline()
file.close()
ind = []

for i in range(len(a)):
    if a[i] == 'A' or a[i] == 'B':
        ind.append(i)

maxl = ind[3]
for i in range(len(ind) - 4):
    l = ind[i + 4] - ind[i] - 1
    maxl = max(l, maxl)
maxl = max(maxl, len(a[ind[-4] + 1]))

print(maxl)

