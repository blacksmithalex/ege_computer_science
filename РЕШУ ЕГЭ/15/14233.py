def f(x, a, b):
    '''
    :param x: переменная, аналогично задаче
    :param a: левая граница отрезка A
    :param b: правая граница отрезка A
    :return: True / False
    '''
    l1 = not (a <= x <= b)
    l2 = (17 <= x <= 46) and (22 <= x <= 57)
    l3 = a <= x <= b
    return l1 <= (l2 <= l3)

elems = set()
for a in range(100):
    for b in range(a + 1, 100):
        flag = True
        for x in range(300):
            x = x / 2
            if f(x, a, b) == False:
                flag = False
        if flag:
            elems.add(b - a)
print(min(elems))