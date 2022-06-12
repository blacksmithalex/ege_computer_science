file = open('26.txt')
a1, alls = [], set()
N = int(file.readline())
for _ in range(N):
    r = int(file.readline())
    if r % 2 != 0:
        a1.append(r)
    alls.add(r)
file.close()
N = len(a1)

count, mavg = 0, 0
for i in range(N):
    for j in range(i + 1, N):
        avg = (a1[i] + a1[j]) // 2
        if avg in alls:
            count += 1
            if avg > mavg:
                mavg = avg
print(count, mavg)
