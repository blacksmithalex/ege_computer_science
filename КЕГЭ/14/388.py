alp = '012345'
for x in alp:
    for y in alp:
        a1 = int('10' + x + y + x, 6)
        a2 = int(y + '11' + x, 7)
        if a1 == a2:
            print(x, y)