a = '2' + '9' * 100
while '19' in a or '299' in a or '3999' in a:
    a = a.replace('19', '2', 1)
    a = a.replace('299', '3', 1)
    a = a.replace('3999', '1', 1)

print(a)




