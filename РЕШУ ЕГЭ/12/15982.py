a = '1' * 82
while '11111' in a or '888' in a:
    if '11111' in a:
        a = a.replace('11111', '88', 1)
    elif '888' in a:
        a = a.replace('888', '8')
print(a)