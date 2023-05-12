alp = '0123456789ab'
for x in alp:
    a1 = int('2ab' + x, 12)
    a2 = int(x + '8e', 17)
    if (a1 + a2) % 27 == 0:
        print(x, (a1 + a2) // 27)