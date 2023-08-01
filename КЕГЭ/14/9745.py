alp = '0123456789abcdefghi'
for x in alp:
    a1 = int('98' + x + '79641', 19)
    a2 = int('36' + x + '14', 19)
    a3 = int('73' + x + '4', 19)
    if (a1 + a2 + a3) % 18 == 0:
        print(x, (a1 + a2 + a3) // 18)

