def f(x, a, b):
    '''
    :param x: переменная x
    :param a: левая граница отрезка A:= [a, b]
    :param b: правая граница отрезка A:= [a, b]
    :return: True / False
    '''
    l1 = 4 <= x <= 15
    l2 = 12 <= x <= 20
    l3 = a <= x <= b
    return (l1 and l2) <= l3

lens = set()
for a in range(100):
    for b in range(a + 1, 100):
        flag = True
        for x in range(200):
            x = x / 2
            if f(x, a, b) == False:
                flag = False
        if flag == True:
            lens.add(b - a)
print(min(lens))



