def f(a):
    while '1111' in a:
        a = a.replace('1111', '22', 1)
        a = a.replace('222', '1', 1)
    return a

for i in range(201, 300):
    a = '1' * i
    print(i, f(a).count('1'))




