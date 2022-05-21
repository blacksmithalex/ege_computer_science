file = open('24.txt')
a = file.readline()
file.close()

ind = []
for i in range(1, len(a) - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        ind.append(i)

M = 0
for i in range(len(ind) - 1):
    if ind[i + 1] - ind[i] > M:
        M = ind[i + 1] - ind[i]
print(M)
