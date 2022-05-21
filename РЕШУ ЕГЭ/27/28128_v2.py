file = open('28128_A.txt')
a01, a02, a1, a2 = 0, 0, 0, 0
N = int(file.readline())
for _ in range(N):
    a = int(file.readline())
    if a % 3 == 0:
        if a > a01:
            a02 = a01
            a01 = a
        elif a > a02:
            a02 = a
    elif a % 3 == 1 and a > a1:
        a1 = a
    elif a % 3 == 2 and a > a2:
        a2 = a

print(max(a01 + a02, a1 + a2))