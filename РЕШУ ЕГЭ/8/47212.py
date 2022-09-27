def f(x):
    ind = x.find('6')
    if ind == 0:
        if int(x[ind + 1]) % 2 != 0:
            return False
        else:
            return True
    elif ind == 4:
        if int(x[ind - 1]) % 2 != 0:
            return False
        else:
            return True
    else:
        if int(x[ind - 1]) % 2 != 0 or int(x[ind + 1]) % 2 != 0:
            return False
        else:
            return True

N = ['0', '1', '2', '3', '4', '5', '6', '7']

count = 0
for x1 in N[1:]:
    for x2 in N:
        for x3 in N:
            for x4 in N:
                for x5 in N:
                    x = x1 + x2 + x3 + x4 + x5
                    if x.count('6') != 1:
                        continue
                    if f(x):
                        count += 1
print(count)







