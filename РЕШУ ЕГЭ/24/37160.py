def f(n):
    '''n - натуральное число; return:: делитель, если он есть / -1 в противном случае'''
    for d in range(18, n, 10):
        if n % d == 0:
            return d
    return -1

count, n = 0, 500000 + 1
while count != 5:
    div = f(n)
    if div != -1:
        print(n, div)
        count += 1
    n += 1