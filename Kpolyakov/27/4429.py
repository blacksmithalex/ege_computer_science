def gcd(a, b):
    if a % b == 0 or b % a == 0:
        return min(a, b)
    elif a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)
def lcm(a, b):
    return a * b // gcd(a, b)

file = open('test.txt')
N, a = int(file.readline()), []
for _ in range(N):
    a.append([int(x) for x in file.readline().split()])
file.close()
LCM = []
for group in a:
    group_lcm = []
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            group_lcm.append(lcm(group[i], group[j]))
    LCM.append(group_lcm)
Diff5, Diff7 = [[] for _ in range(5)] ,  [[] for _ in range(7)]

maxS = 0
for group in LCM:
    group = sorted(group)
    maxS += group[-1]
    for i in range(len(group) - 1):
        diff = group[-1] - group[i]
        Diff5[diff % 5].append(diff)
        Diff5[diff % 5].sort()
        Diff7[diff % 7].append(diff)
        Diff7[diff % 7].sort()

print(LCM)
print(Diff5)
print(Diff7)
print(maxS)
print(maxS % 5, maxS % 7)





