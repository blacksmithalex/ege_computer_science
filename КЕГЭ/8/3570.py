alp = sorted('СОЛНЦЕ')
count = 1
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    a = a1 + a2 + a3 + a4 + a5
                    print(count, a)
                    count += 1
                    if a.count('Е') <= 1 and a.count('Л') == 0:
                        quit()