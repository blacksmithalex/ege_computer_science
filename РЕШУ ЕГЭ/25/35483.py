from math import sqrt
def isfit(n):
    count = 0
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            if d % 2 != 0:
                count += 1
            if n // d % 2 != 0 and n // d != d:
                count += 1
            if count > 5:
                return False
    if count == 5:
        return True
    return False

for n in range(35000000, 40000000 + 1):
    if isfit(n):
        print(n)

"""-----------------------------------------------"""
#будем рассматривать числа n = p^4 * 2^k, где p < 100, k < 30
def P(n):
    '''возвращает в виде списка все простые числа до n не включительно'''
    p = []
    for x in range(2, n):
        flag = True
        for d in range(2, x):
            if x % d == 0:
                flag = False
                break
        if flag == True:
            p.append(x)
    return p

res = []
primes = P(100)
for p in primes:
    for k in range(31):
        n = p ** 4 * 2 ** k
        if 35000000 <= n <= 40000000:
            res.append(n)
for x in sorted(res):
    print(x)

