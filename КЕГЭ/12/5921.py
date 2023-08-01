a = '7' * 333
while '66' in a or '77777' in a:
    if '66' in a:
        a = a.replace('66', '7', 1)
    else:
        a = a.replace('77777', '676676', 1)
p = 1
for x in a:
    p *= int(x)
print(p)