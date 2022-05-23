def check(a):
    if a[0] == 'А':
        return False
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return False
    return True


l = ['А', 'Б', 'В','Г']
count = 0
for a1 in l:
    for a2 in l:
        for a3 in l:
            for a4 in l:
                for a5 in l:
                    for a6 in l:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if check(a):
                            count += 1
print(count)