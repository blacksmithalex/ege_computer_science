from math import sqrt
def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return div

def Cubic(n):
    for d in range(2, n + 1):
        if n == d * d * d:
            return d
        if n < d * d * d:
            return -1

def Numof(n, div):
    count = 0
    for d in div:
        R = Cubic(d)
        if R != -1 and R % 2 != 0:
            count += 1
    return count

for n in range(228224, 531135 + 1):
    div = dividers(n)
    count = Numof(n, div)
    if count >= 4:
        print(n, count, max(div))










