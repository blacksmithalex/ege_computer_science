alp = 'ГЕПАРД'
count = 0
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    a = a1 + a2 + a3 + a4 + a5
                    if a1 != 'А' and a5 != 'Е' and a.count('Г') == 1:
                        count += 1
print(count)