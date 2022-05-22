def edge_dist(i, j):
    '''ищет минимальное растояние от клетки до краев таблицы'''
    return min(i, j, 10000 - i - 1, 10000 - j - 1)

def Mgroups(line):
    '''выдает двумерный список, содержащий списки из двух элементов (начало и конец групп,
    которые имеют максимальную длинну из единиц)'''
    s = ''.join([str(x) for x in line])
    Ml = max([len(x) for x in s.split('0')])
    res = []
    for i in range(len(s)):
        if s[i: i + Ml] == '1' * Ml:
            res.append([i, i + Ml - 1])
    return res

a = [[0] * 10000 for _ in range(10000)]
file = open('26.txt')
N = int(file.readline())
for _ in range(N):
    i, j = [int(x) - 1 for x in file.readline().split()]
    a[i][j] = 1
file.close()

L, Nline, MinDist = 0, 0, 1e16
for i in range(10000):
    groups = Mgroups(a[i])
    localMinDist = 1e16
    for g in groups:
        l, r = g[0], g[1]
        localDist = min(edge_dist(i, l), edge_dist(i, r))
        if r - l + 1 > L:
            L = r - l + 1
            Nline = i
            MinDist = localDist
        elif r - l + 1 == L:
            if MinDist > localDist:
                MinDist = localDist
                Nline = i
print(Nline + 1, MinDist)

#Ответ: 6539 287
#Код можно переписать оптимальнее, если использовать словари, а не задавать двумерный список
#10000 на 10000 значений


