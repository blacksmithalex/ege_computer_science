from math import sqrt
def R(n):
    chet, nech = set(), set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            if d % 2 == 0:
                chet.add(d)
            else:
                nech.add(d)
            if (n // d) % 2 == 0:
                chet.add(n // d)
            else:
                nech.add(n // d)
    if len(chet) != len(nech) or len(chet) < 70 or len(nech) < 70:
        return -1
    else:
        return(min(min([x for x in chet if x > 1000]), min([x for x in nech if x > 1000])))

for n in range(326496, 649632 + 1):
    res = R(n)
    if res != -1:
        print(n, res)




