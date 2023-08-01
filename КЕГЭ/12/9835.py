for n in range(4, 10000):
    a = '1' + '8' * n
    while '18' in a or '388' in a or '888' in a:
        if '18' in a:
            a = a.replace('18', '8', 1)
        if '388' in a:
            a = a.replace('388', '81', 1)
        if '888' in a:
            a = a.replace('888', '3', 1)
    if a.count('1') == 3:
        print(n)
        break