a = '7' * 104
while '33333' in a or '777' in a:
    if '33333' in a:
        a = a.replace('33333', '7', 1)
    else:
        a = a.replace('777', '3', 1)
print(a)