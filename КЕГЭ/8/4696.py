def f(a):
    ind = a.find('6')
    if ind == 0:
       next = int(a[ind + 1])
       return next % 2 == 0
    elif ind == 4:
        prev = int(a[ind - 1])
        return prev % 2 == 0
    else:
        next = int(a[ind + 1])
        prev = int(a[ind - 1])
        return (prev % 2 == 0) and (next % 2 == 0)

count = 0
alp = '01234567'
for a1 in alp[1:]:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    a = a1 + a2 + a3 + a4 + a5
                    if a.count('6') == 1 and f(a):
                        count += 1
print(count)
