l = ['А', 'К', 'Л', 'О', 'Ш']
n = 1
for a1 in l:
    for a2 in l:
        for a3 in l:
            for a4 in l:
                for a5 in l:
                    a = a1 + a2 + a3 + a4 + a5
                    print(n, a)
                    n += 1
