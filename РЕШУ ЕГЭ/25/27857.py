from math import sqrt
def dividers(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

Mcount, Mn = 0, 0
for n in range(84130, 84052 - 1, -1):
    div = dividers(n)
    if len(div) >= Mcount:
        Mcount = len(div)
        Mn = n

print(Mcount, Mn)

