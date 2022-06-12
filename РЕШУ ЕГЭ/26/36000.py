file = open('inf_26_04_21_26.txt')
a0, a1 = [], []
alls = set()
N = int(file.readline())
for _ in range(N):
    r = int(file.readline())
    alls.add(r)
    if r % 2 == 0:
        a0.append(r)
    else:
        a1.append(r)
file.close()

count, smax = 0, 0
for i in range(len(a0)):
    for j in range(len(a1)):
        s = a0[i] + a1[j]
        if s in alls:
            count += 1
            if s > smax:
                smax = s
print(count, smax)

