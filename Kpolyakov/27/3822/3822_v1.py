from math import factorial
def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
def sumC(n):
    res = 0
    start = 3
    while start <= n:
        res += C(n, start)
        start += 3
    return res

file = open('test.txt')
n = int(file.readline())
count0, count1, count2 = 0, 0, 0
for _ in range(n):
    r = int(file.readline())
    if r % 3 == 0:
        count0 += 1
    elif r % 3 == 1:
        count1 += 1
    else:
        count2 += 1
file.close()

R0 = 2 ** count0 - 1
R1 = sumC(count1)
R2 = sumC(count2)

R3 = 0
for k in range(1, count1 + 1):
    for t in range(1, count2 + 1):
        if (k + 2 * t) % 3 == 0:
            R3 += C(count1, k) * C(count2, t)

print(R0 + R1 + R2 + R3 + R0 * R1 + R0 * R2 + R0 * R3)