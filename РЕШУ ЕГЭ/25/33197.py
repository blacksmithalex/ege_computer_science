from math import sqrt
def isTrue(n):
    count = 0
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            if n // d - d <= 100:
                count += 1
                if count >= 3:
                    return True
    return False

for n in range(1000000, 2000000 + 1):
    if isTrue(n):
        print(n)


