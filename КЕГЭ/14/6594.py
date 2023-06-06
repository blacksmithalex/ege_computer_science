alp = '0123456789abc'
for x in alp:
    a1 = int('753' + x + '2', 13)
    a2 = int('2' + x + '173', 13)
    if (a1 + a2) % 12 == 0:
        print(x, (a1 + a2) // 12)


