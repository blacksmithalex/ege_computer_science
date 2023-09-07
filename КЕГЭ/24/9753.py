file = open('24_9753.txt')
a = file.readline()
file.close()
ind = []
for i in range(len(a)):
    if a[i] == 'Y':
        ind.append(i)

mlen = ind[150]
for i in range(len(ind) - 151):
    l = ind[i + 151] - ind[i] - 1
    if mlen < l:
        mlen = l
mlen = max(mlen, len(a[ind[-151] + 1:]))

print(mlen)