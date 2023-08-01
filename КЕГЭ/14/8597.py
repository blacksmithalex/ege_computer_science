alp = '0123456789abcde'
for x in alp:
    a1 = int('97968'+ x + '13', 15)
    a2 = int('7' + x + '213' , 15)
    if (a1 + a2) % 11 == 0:
        print(x)
