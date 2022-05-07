file = open('26.txt')
N = int(file.readline())
INF = 1e16
start, finish, alltimes = {}, {}, set()
for _ in range(N):
    s, f = [int(x) for x in file.readline().split()]
    if f == 0:
        f = INF
    start[s] = start.get(s, 0) + 1
    finish[f] = finish.get(f, 0) + 1
    alltimes.add(s)
    alltimes.add(f)
file.close()
alltimes = sorted(alltimes)

numofP = {}
numofP[alltimes[0]] = start[alltimes[0]]
for i in range(1, len(alltimes)):
    numofP[alltimes[i]] = numofP[alltimes[i - 1]]
    if alltimes[i] in start:
        numofP[alltimes[i]] += start[alltimes[i]]
    if alltimes[i] in finish:
        numofP[alltimes[i]] -= finish[alltimes[i]]

sec_in_week = 7 * 24 * 60 * 60
itterations = [x for x in numofP.keys() if 1633305600 <= x <= 1633305600 + sen_in_week]
R = [[numofP[x], x] for x in itterations]

print(sorted(R))

ind1 = alltimes.index(1633905186)
print(alltimes[ind1 + 1] - alltimes[ind1])
ind2 = alltimes.index(1633905171)
print(alltimes[ind2 + 1] - alltimes[ind2])
ind3= alltimes.index(1633904848)
print(alltimes[ind3 + 1] - alltimes[ind3])

#ответ 5000 46



