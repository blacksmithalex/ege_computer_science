from math import sqrt
def isprime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True
def f(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    count = 0
    for d in div:
        if d != 1 and isprime(d):
            count += 1
    return count > 3

count = 0
for n in range(2, 20000 + 1):
    if f(n):
        count += 1
print(count)

