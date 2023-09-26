def f(a):
    for i in range(len(a) - 1):
        if (int(a[i]) + int(a[i + 1])) % 2 == 0:
            return False
    return True

count = 0
alp = '0234567'
for a1 in alp[1:]:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    a = a1 + a2 + a3 + a4 + a5
                    if len(set(a)) == 5 and f(a):
                        count += 1
print(count)