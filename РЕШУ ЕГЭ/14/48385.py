alp = '0123456789abc'
for x in alp:
    for y in alp:
        a1 = int('8' + x + '78' + y, 13)
        a2 = int('79' + x + y +  '7', 18)
        if (a1 + a2) % 9 == 0:
            print(x, y, (a1 + a2) // 9)

