from math import sqrt
def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

count = 0
n = 500000000 - 1
while count != 5:
    div = dividers(n)
    if len(div) >= 6:
        print(div[-6], len(div))
        count += 1
    n -= 1

