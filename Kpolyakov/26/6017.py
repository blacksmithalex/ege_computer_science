file = open('26-99.txt')
N, M = [int(x) for x in file.readline().split()]
a = sorted([int(x) for x in file], reverse=True)
takes = [False] * N

nauto = 0
weights = []
S = 0
while False in takes:
    for i in range(N):
        if S + a[i] <= M and takes[i] == False:
            S += a[i]
            takes[i] = True
    nauto += 1
    weights.append(S)
    S = 0
print(nauto, weights[-2])








