#Число имеет вид num = p^4 * 2^n, где p - простое >=3, n - натуральное или 0
#С помощью достаточно грубой оценки можно получить, что p мы ищем в пределах 100, n < 30
from math import sqrt
def isPrime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

res = []
for deg_two in range(30):
    for p in range(3, 100):
        if not isPrime(p):
            continue
        num = p ** 4 * 2 ** deg_two
        if 45000000 <= num <= 50000000:
            res.append(num)
for p in sorted(res):
    print(p)

