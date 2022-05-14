from math import sqrt
def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

def isFit(div):
    for i in range(len(div) - 1):
        if div[i + 1] - div[i] != 2:
            return False
    return True

for n in range(834567, 1143210 + 1):
    div = dividers(n)
    if len(div) > 1 and isFit(div):
        print(n, div[-1])

