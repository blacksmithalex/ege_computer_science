a = 'AB' * 52
while ('AA' in a) or ('BB' in a) or ('AB' in a):
    a = a.replace('AA', 'B')
    a = a.replace('BB', 'A')
    a = a.replace('AB', 'BA')
print(a)