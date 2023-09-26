alp = sorted('МАНГУСТ')
n = 1
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    for a6 in alp:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if a1 != 'У' and a.count('М') == 2 and a.count('Г') <= 1:
                            print(n, a)
                        n += 1
