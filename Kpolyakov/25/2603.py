from math import sqrt
def dividers(n):
    res = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)

def isprime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

div1, div2 = 0, int(1e6)
for n in range(523456, 578925 + 1):
    div = dividers(n)
    if len(div) == 4:
        if isprime(div[1]) and isprime(div[2]):
            if div[2] - div[1] < div2 - div1:
                div1, div2 = div[1], div[2]

print(div1, div2)

