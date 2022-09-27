def f(a):
    for i in range(len(a) - 1):
        if a[i] in glas and a[i + 1] in glas:
            return False
        elif a[i] in sogl and a[i + 1] in sogl:
            return False
    return True

def g(a):
    for x in a:
        if a.count(x) != 'РОСОМАХА'.count(x):
            return False
    return True

al = ['С', 'Х', 'Р', 'О', 'М', 'А']
glas = ['О', 'А']
sogl = ['С', 'Х', 'Р', 'М']

count = 0
for a1 in al:
    for a2 in al:
        for a3 in al:
            for a4 in al:
                for a5 in al:
                    for a6 in al:
                        for a7 in al:
                            for a8 in al:
                                a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
                                if f(a) and g(a):
                                    count += 1
print(count)






