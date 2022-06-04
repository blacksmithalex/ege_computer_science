a = '3' * 68

while '999' in a or '333' in a:
    if '333' in a:
        a = a.replace('333', '9', 1)
    else:
        a = a.replace('999', '3', 1)
print(a)