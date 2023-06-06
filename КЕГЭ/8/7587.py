alp = 'АВЛОР'
count = 1
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                a = a1 + a2 + a3 + a4
                print(count, a)
                count += 1
                if a1 == 'Л':
                    quit()