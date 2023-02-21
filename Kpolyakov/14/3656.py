def f(n, d):
    res = ''
    while n != 0:
        res += str(n % d)
        n //= d
    return res[::-1]
def odd_nums(a):
    count = 0
    for x in a:
        if int(x) % 2 != 0:
            count += 1
    return count

n = 456
for d in range(2, 10 + 1):
    a = f(n, d)
    print(d, odd_nums(a))