alp = sorted('КОМПЬЮТЕР')
n = 1
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    a = a1 + a2 + a3 + a4 + a5
                    if n % 2 != 0 and a1 != 'Ь' and a.count('К') == 2:
                        print(n, a)
                    n += 1