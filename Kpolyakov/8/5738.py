from itertools import product
def f(a):
    nglas, nsogl = 0, 0
    for x in a:
        if x in glas:
            nglas += 1
        else:
            nsogl += 1
    return nglas < nsogl
def g(a):
    if a[0] == 'Ш' and a[1] in sogl:
        return False
    if a[-1] == 'Ш' and a[-2] in sogl:
        return False
    for i in range(1, 5):
        if a[i] == 'Ш' and (a[i - 1] in sogl or a[i + 1] in sogl):
            return False
    return True
glas = list('ИАЕ')
sogl = list('ТМШВСК')

count = 0
for a in product('ТИМАШЕВСК', repeat = 6):
    a = ''.join(a)
    if f(a) and g(a):
        count += 1
print(count)




