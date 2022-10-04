a = '1' * 81
while '1111' in a or '88888' in a:
    if '1111' in a:
        a = a.replace('1111', '888', 1)
    else:
        a = a.replace('88888', '888', 1)

print(a)

