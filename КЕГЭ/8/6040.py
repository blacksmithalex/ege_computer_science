def f(a):
    '''
    :param a: число в строком виде
    :return: True / False
    '''
    for i in range(len(a) - 1):
        if (int(a[i]) + int(a[i + 1])) % 2 == 0:
            return False
    return True

alp = '0123456'
count = 0
for a1 in alp[1:]:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    for a6 in alp:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if a.count('6') == 1 and f(a):
                            count += 1
print(count)