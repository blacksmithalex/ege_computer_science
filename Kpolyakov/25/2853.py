from math import sqrt
def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

p1, p2 = 0, 10**6
for n in range(309829, 365874 + 1):
    div = dividers(n)
    if len(div) == 2:
        p1new, p2new = div
        if p2new - p1new < p2 - p1:
            p1, p2 = p1new, p2new
print(p1, p2)




