from math import ceil
file = open('26-j2.txt')
N = int(file.readline())
a = sorted([int(x) for x in file])
file.close()

l = a.index(ceil(sum(a) / N))
r = N // 2
mid = a[r]
while a[r] == mid:
    r += 1

print(r - l)

