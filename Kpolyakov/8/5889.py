def f(a):
    inds = []
    for i in range(len(a)):
        if a[i] in list('ОЕА'):
            inds.append(i)
    for i in range(len(inds) - 1):
        if inds[i + 1] - inds[i] == 1:
            return False
    return True

count = 0
alp = list('КОНФЕТА')
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    a = a1 + a2 + a3 + a4 + a5
                    num = a.count('О') + a.count('Е') + a.count('А')
                    if num >= 2 and f(a):
                        count += 1
print(count)
