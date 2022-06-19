from math import sqrt
def dividers(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div, reverse= True)[1:]

def semiperfect(n):
    div = dividers(n)
    S = 0
    for d in div:
        if S + d <= n:
            S += d
    return S == n

count = 0
for n in range(2, 2000 + 1):
    if semiperfect(n):
        count += 1

print(count)