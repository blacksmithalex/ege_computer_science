alp = '0123456789abcde'
for x in alp:
    a1 = int('123' + x + '5', 15)
    a2 = int('1' + x + '233', 15)
    if (a1 + a2) % 14 == 0:
        print(x, (a1 + a2) // 14)

