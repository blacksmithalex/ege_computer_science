al = ['А', 'О', 'У']
count = 1
for a1 in al:
    for a2 in al:
        for a3 in al:
            for a4 in al:
                for a5 in al:
                    a = a1 + a2 + a3 + a4 + a5
                    print(count, a)
                    count += 1