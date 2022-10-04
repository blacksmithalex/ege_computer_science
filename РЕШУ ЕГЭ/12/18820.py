a = '9' * 65
while '999' in a or '222' in a:
    if '222' in a:
        a = a.replace('222', '9', 1)
    else:
        a = a.replace('999', '2', 1)

print(a)

