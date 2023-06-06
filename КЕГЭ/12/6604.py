def f(a):
    while '>1' in a or '>2' in a or '>3' in a:
        if '>1' in a:
            a = a.replace('>1', '2>', 1)
        if '>2' in a:
            a = a.replace('>2', '3>', 1)
        if '>3' in a:
            a = a.replace('>3', '11>', 1)
    return a
def dividers(n):
    div = []
    for d in range(2, n):
        if n % d == 0:
            div.append(d)
    return div

for m in range(300):
    a = '>' + '1' * 15 + '2' * 35 + '3' * m
    r = f(a)[:-1]
    S = 0
    for x in r:
        S += int(x)
    if len(dividers(S)) == 3:
        print(m)
        break