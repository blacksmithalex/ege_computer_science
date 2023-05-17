from itertools import combinations
from math import sqrt
def check(divs, n):
    ld = len(divs)
    for l in range(1, ld + 1):
        vars = combinations(divs, r = l)
        for v in vars:
            if sum(v) == n:
                return True
    return False
def dividers(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)[:-1]
count = 0
for n in range(2, 2000 + 1):
    div = dividers(n)
    if check(div, n):
        count += 1
print(count)

