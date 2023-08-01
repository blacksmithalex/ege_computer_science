count = 0 #кол-во подход. n
for n in range(1, 100 + 1):
    a = '1' + '0' * n
    while '01' in a or '1' in a:
        if '10' in a:
            a = a.replace('10', '0001', 1)
        else:
            if '1' in a:
                a = a.replace('1', '0', 1)
    if len(a) % 7 == 0:
        count += 1
print(count)
