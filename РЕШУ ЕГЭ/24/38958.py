file = open('24.txt')
a = file.readline()
file.close()
ind = []
for i in range(len(a)):
    if a[i] == 'A':
        ind.append(i)

mlen = ind[1]
for i in range(len(ind) - 2):
    l = ind[i + 2] - ind[i] - 1
    if mlen < l:
        mlen = l
mlen = max(mlen, len(a[ind[-2] + 1:]))

print(mlen)