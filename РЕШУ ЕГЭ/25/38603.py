from math import sqrt
def f(n):
    for d in range(2,int(sqrt(n)) + 1):
        if n % d == 0:
            return n // d + d
    return 0

count = 0
n = 700000 + 1
while count != 5:
    M = f(n)
    if M % 10 == 8:
        print(n, M)
        count += 1
    n += 1