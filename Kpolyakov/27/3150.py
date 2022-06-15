file = open('27-44b.txt')
N = int(file.readline())
S1, S2, S3 = 0, 0, 0
dmins1 = []
dmins2 = []

for _ in range(N):
    a, b, c = sorted([int(x) for x in file.readline().split()])
    S1 += a
    S2 += b
    S3 += c
    dmins1.append([c - a, c - b])
    dmins2.append([c - b, c - a])

dmins1 = sorted(dmins1)
dmins2 = sorted(dmins2)

print(dmins1[:10])
print(dmins2[:10])

print(S3 - 25 - 27)