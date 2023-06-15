alp = '0123456789abcde'
for x in alp:
    a1 = int('99658' + x + '29', 15)
    a2 = int('102' + x + '023', 15)
    if (a1 + a2) % 14 == 0:
        print(x, (a1 + a2) // 14)