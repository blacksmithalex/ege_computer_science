l = ['Р', 'Е', 'Г', 'И', 'Н', 'А']
count = 0
for a1 in l:
    for a2 in l:
        for a3 in l:
            for a4 in l:
                for a5 in l:
                    a = a1 + a2 + a3 + a4 + a5
                    if a.count('Р') == 1 and a.count('Г') == 1 and a.count('Н') <= 1:
                        count += 1
print(count)
