#Все числа имеют вид num = 2p^2, где p - простое, отличное от 2
#Достаточно грубой оценкой можно получить, что p мы ищем не более 8000
from math import sqrt
def isPrime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

res = []
for p in range(3, 8000):
    if not isPrime(p):
        continue
    num = 2 * p ** 2
    if 101000000 <= num <= 102000000:
        res.append(num)

for p in sorted(res):
    print(p)