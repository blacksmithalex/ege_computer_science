from math import sqrt
def dividers(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

for n in range(110203, 110245 + 1):
    div = dividers(n)
    chet = []
    for d in div:
        if d % 2 == 0:
            chet.append(d)
    if len(chet) == 4:
        print(*chet)