def f(a):
    while '111' in a:
        a = a.replace('111', '22', 1)
        a = a.replace('222', '11', 1)
    return a

bound = 1000
count1, mina = bound, ''
for n in range(101, bound):
    a = '1' * n
    fa = f(a)
    if fa.count('1') < count1:
        count1, mina = fa.count('1'), a

print(len(mina))


