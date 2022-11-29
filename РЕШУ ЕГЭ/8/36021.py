count = 0
for a1 in ['В', 'И', 'Н', 'Я']:
    for a2 in ['В', 'И', 'Ш', 'Н', 'Я']:
        for a3 in ['В', 'И', 'Ш', 'Н', 'Я']:
            for a4 in ['В', 'И', 'Ш', 'Н', 'Я']:
                for a5 in ['В', 'И', 'Ш', 'Н', 'Я']:
                    for a6 in ['И', 'Я']:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if a.count('В') <= 1:
                            count += 1
print(count)
