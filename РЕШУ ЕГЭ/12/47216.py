def f(a):
    while '>1' in a or '>2' in a or '>0' in a:
        if '>1' in a:
            a = a.replace('>1', '22>', 1)
        if '>2' in a:
            a = a.replace('>2', '2>', 1)
        if '>0' in a:
            a = a.replace('>0', '1>', 1)
    return a
def isPrime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

for n in range(100):
    a = '>' + '0' * 39 + '1' * n + '2' * 39
    a = f(a)
    S = sum([int(x) for x in a[:-1]])
    if isPrime(S):
        print(n)
        break