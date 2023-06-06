alp = 'НИЧЬЯ'
count = 0
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    for a6 in alp:
                        for a7 in alp:
                            a = a1 + a2 + a3 + a4 + a5 + a6 + a7
                            inds = []
                            for i in range(len(a)):
                                if a[i] in 'ИЯ':
                                    inds.append(i)
                            if len(inds) == 2 and inds[1] - inds[0] != 1:
                                count += 1
print(count)

