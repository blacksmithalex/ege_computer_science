from math import sqrt
def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

for n in range(210235, 210300 + 1):
    div = dividers(n)
    if len(div) == 4:
        print(*div)

