from math import sqrt
def isPrime(n):
    for d in range(2, int(sqrt(n) + 1)):
        if n % d == 0:
            return False
    return True

def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return div

def isFit(n):
    div = dividers(n)
    if len(div) != 2:
        return False
    for d in div:
        if not isPrime(d):
            return False
    return True

count = 0
M = 0
for n in range(125697, 190234 + 1):
    if isFit(n):
        count += 1
        M = n
print(count, M)

