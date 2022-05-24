l = ['О', 'Н', 'И', 'К', 'С']
count = 0
for a1 in l:
    for a2 in l:
        for a3 in l:
            for a4 in l:
                a = a1 + a2 + a3 + a4
                if a.count('С') == 3 and a.count('О') == 1:
                    count += 1
for a1 in l:
    for a2 in l:
        for a3 in l:
            for a4 in l:
                for a5 in l:
                    a = a1 + a2 + a3 + a4 + a5
                    if a.count('С') == 3 and a.count('О') == 1:
                        count += 1

for a1 in l:
    for a2 in l:
        for a3 in l:
            for a4 in l:
                for a5 in l:
                    for a6 in l:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if a.count('С') == 3 and a.count('О') == 1:
                            count += 1

print(count)
