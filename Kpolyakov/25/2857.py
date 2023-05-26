from math import sqrt
def dividers(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)
def iscube(n):
    '''
    :param n: целое неотрицательное число
    :return: -1, если n не является 3 степенью целого числа, в противном случае - результат взятия корня 3 степени
    '''
    l = -1
    r = n
    while l + 1 != r:
        c = (l + r) // 2
        if c**3 < n:
            l = c
        else:
            r = c
    if r**3 == n:
        return r
    else:
        return -1

for n in range(228224, 531135 + 1):
    div = dividers(n)
    count3 = 0
    m3 = 0
    for d in div:
        res = iscube(d)
        if res != -1 and res % 2 != 0:
            count3 += 1
            m3 = max(m3, d)
    if count3 >= 4:
        print(n, count3, m3)
