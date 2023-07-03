alp = '012345678'
for x in alp:
    for y in alp:
        a1 = int('88' + x + '4' + y, 9)
        a2 = int('7' + x + '44' + y, 11)
        if (a1 + a2) % 61 == 0:
            print(x, y, (a1 + a2) // 61)

