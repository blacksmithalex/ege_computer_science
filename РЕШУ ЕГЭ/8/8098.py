a = ['С', 'Л', 'О', 'Н']
count = 0
for s1 in a:
    for s2 in a:
        for s3 in a:
            for s4 in a:
                for s5 in a:
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count('С') == 1:
                        count += 1
print(count)