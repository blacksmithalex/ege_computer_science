alp = '01234567'
for x in alp:
    for y in alp:
        a1 = int(x + '01' + y + '4', 9)
        a2 = int(x + y + '544', 8)
        if (a1 + a2) % 89 == 0:
            print(x, (a1 + a2) // 89)

