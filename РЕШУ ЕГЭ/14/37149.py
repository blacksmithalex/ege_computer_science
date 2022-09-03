def f(n):
    '''перевод из десятиричной в пятиричную'''
    res = []
    while n != 0:
        res.append(n % 5)
        n //= 5
    return res[::-1]

a = 4 * 625**9 - 25**15 + 2 * 5**11 - 7
a = f(a)
print(a.count(4))
