file = open('26.txt')
N = int(file.readline())
a = sorted(set([int(x) for x in file]), reverse= True)
file.close()

count = 1
cur, prev = 1, 0
while cur < len(a):
    if a[prev] - a[cur] >= 3:
        count += 1
        prev = cur
    cur += 1
print(count, a[prev])

