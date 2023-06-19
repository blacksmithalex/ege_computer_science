from math import sqrt
from fnmatch import fnmatch
def dividers(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            if fnmatch(str(d), '???0'):
                div.add(d)
            if fnmatch(str(n // d), '???0'):
                div.add(n // d)
    return len(div)

for n in range(5 * 10**5, 10**6 + 1):
    n_divs = dividers(n)
    if n_divs > 45:
        print(n, n_divs)



