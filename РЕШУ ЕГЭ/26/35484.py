file = open('26.txt')
N = int(file.readline())
chet, alls = [], set()
for _ in range(N):
    r = int(file.readline())
    if r % 2 == 0:
        chet.append(r)
    alls.add(r)

count, mavg = 0, 0
for i in range(len(chet)):
    for j in range(i + 1, len(chet)):
        avg = (chet[i] + chet[j]) // 2
        if avg in alls:
            count += 1
            if avg > mavg:
                mavg = avg
print(count, mavg)


