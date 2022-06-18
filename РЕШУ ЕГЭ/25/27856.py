from math import sqrt
def f(n):
    d = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0 and i % 2 != 0:
            d.append(i)
        if n % i == 0 and (n // i) % 2 != 0 and n // i != i:
            d.append(n // i)
    return (sorted(d))

for i in range(95632, 95650 + 1):
    if len(f(i)) == 6:
        print(*f(i))