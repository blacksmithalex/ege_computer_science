count = 0
alp = '0123456'
for a1 in alp[1:]:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                        a = a1 + a2 + a3 + a4 + a5
                        s0 = sum([int(x) for x in a if int(x) % 2 == 0])
                        s1 = sum([int(x) for x in a if int(x) % 2 != 0])
                        if a.count('6') == 1 and s1 > s0:
                            count += 1
print(count)