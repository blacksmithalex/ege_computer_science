for n in range(100):
    a = '>' + '0' * 40 + '1' * n + '2' * 40
    while '>1' in a or '>2' in a or '>0' in a:
        if '>1' in a:
            a = a.replace('>1', '22>', 1)
        if '>2' in a:
            a = a.replace('>2', '2>', 1)
        if '>0' in a:
            a = a.replace('>0', '1>', 1)
    sdigits = 0
    for x in a[:-1]:
        sdigits += int(x)
    print(n, sdigits)
