from math import sqrt
def num_of_chet(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            if d % 2 == 0:
                div.add(d)
            if (n // d) % 2 == 0:
                div.add(n // d)
    return len(div)

Mk = 950000000 + 1
count = 0
while count != 5:
    if Mk % 10000 == 0:
        print('Прошло', Mk)
    num = num_of_chet(Mk)
    if num % 2 != 0:
        print(Mk - 950000000)
        count += 1
    Mk += 1

