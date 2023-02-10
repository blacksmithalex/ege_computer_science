file = open('24.txt')
a = file.readline()
file.close()

inds = [i for i in range(len(a)) if a[i] == 'A']
countm = inds[1]

for i in range(len(inds) - 2):
    l = inds[i + 2] - inds[i] - 1
    countm = max(countm, l)

last = len(a[inds[-2] + 1:])
countm = max(countm, last)
print(countm)
