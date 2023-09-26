def f(a):
    ind = a.find('2')
    if ind == 0:
        return int(a[ind + 1]) % 2 == 0
    elif ind == len(a) - 1:
        return int(a[ind - 1]) % 2 == 0
    else:
        return (int(a[ind + 1]) % 2 == 0) and (int(a[ind - 1]) % 2 == 0)


count = 0
alp = '012345'
for a1 in alp[1:]:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    for a6 in alp:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if a.count('2') == 1 and f(a):
                            count += 1
print(count)