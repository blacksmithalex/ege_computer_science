file = open('26_8512.txt')
K = int(file.readline())
N = int(file.readline())
a = []
for _ in range(N):
    start, end = [int(x) for x in file.readline().split()]
    a.append([start, end])
file.close()
a = sorted(a)

ends = [-1] * K
count, lastind = 0, 0
for start, end in a:
    for i in range(K):
        if ends[i] < start:
            count += 1
            ends[i] = end
            lastind = i
            break
print(count, lastind + 1)