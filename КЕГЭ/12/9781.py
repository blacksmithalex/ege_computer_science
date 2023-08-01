smax = 0
for n in range(4, 10000):
    a = '1' + '2' * n
    while '12' in a or '322' in a or '222' in a:
        if '12' in a:
            a = a.replace('12', '2', 1)
        if '322' in a:
            a = a.replace('322', '21', 1)
        if '222' in a:
            a = a.replace('222', '3', 1)
    s = 0
    for x in a:
        s += int(x)
    smax = max(s, smax)
print(smax)