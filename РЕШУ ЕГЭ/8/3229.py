l = ['А', 'К', 'Р', 'У']
count = 1
for a1 in l:
    for a2 in l:
        for a3 in l:
            for a4 in l:
                for a5 in l:
                    a = a1 + a2 + a3 + a4 + a5
                    print(count, a)
                    count += 1
