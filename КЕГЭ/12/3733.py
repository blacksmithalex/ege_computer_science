uniq = set()
for n in range(1, 2000):
    a = '1' * n
    while '1111' in a or '222' in a or '33' in a:
        if '1111' in a:
            a = a.replace('1111', '333', 1)
        elif '222' in a:
            a = a.replace('222', '11', 1)
        elif '33' in a:
            a = a.replace('33', '2', 1)
    uniq.add(a)
print(len(uniq))