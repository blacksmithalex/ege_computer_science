def f(a, b, x):
    '''
    :param a: левая граница отрезка A
    :param b: правая граница отрезка A
    :param x: x, который подставляем
    :return: True, если функция верна, False иначе
    '''
    l1 = 20 <= x <= 30
    l2 = 5 <= x <= 15
    l3 = not (a <= x <= b)
    l4 = 35 <= x <= 50
    return (l1 <= l2) or (l3 <= l4)

res = set()
for a in range(100):
    for b in range(a + 1, 100):
        flag = True
        for x in range(200):
            x = x / 2
            if f(a, b, x) == False:
                flag = False
        if flag == True:
            res.add(b - a)
print(min(res))

