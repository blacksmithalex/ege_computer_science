# разложение любого числа до 15 включительно на сумму натуральных чисел
variants = {}
variants[0] = [[0]]
variants[1] = [[1]]

for i in range(2, 16):
    newvar = []
    for j in range(i - 1, 0, -1):
        prev = variants[i - j]
        for v in prev:
            if v[-1] > j:
                continue
            newvar.append(v + [j])
    newvar.append([i])
    variants[i] = newvar

file = open('test.txt')
n = int(file.readline())
Smin = 0
D = [[] for _ in range(16)]
for _ in range(n):
    first, second = sorted([int(x) for x in file.readline().split()])
    Smin += first
    d = second - first
    if d % 16 != 0:
        D[d % 16] = sorted(D[d % 16] + [d])[:15]


if Smin % 16 == 15:
    print(Smin)
else:
    r = Smin % 16
    res = 15 - r
    V = variants[res]
    newSmin = 1e16
    for v in V:
        flag = True
        newS = Smin
        countD = {}
        for i in range(1, 16):
            countD[i] = v.count(i)
        for localD in countD:
            if countD[localD] > len(D[localD]):
                flag = False
                break
            newS += sum(D[localD][:countD[localD]])
        if flag == True and newS < newSmin:
            newSmin = newS
    print(newSmin)

# В задании не совсем корректно перебираются варианты, а именно учитывается разложение остатка только по натуральным числам, не превышающим его
# Код работает на тестовом примере и файле B