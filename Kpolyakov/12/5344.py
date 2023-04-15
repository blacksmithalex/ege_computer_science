a = '9' * 84
while '33333' in a or '999' in a:
    if '33333' in a:
        a = a.replace('33333', '99', 1)
    else:
        a = a.replace('999', '3', 1)
print(a)