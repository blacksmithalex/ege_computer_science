a = '1' + '0' * 55
while ('1' in a):
    if '10' in a:
        a = a.replace('10', '001', 1)
    else:
        a = a.replace('1', '00', 1)
print(a.count('0'))