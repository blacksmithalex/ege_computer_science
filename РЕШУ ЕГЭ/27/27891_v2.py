file = open('27-B_2.txt')
N = int(file.readline())
m7, m2, m14, m = 0, 0, 0, 0
for _ in range(N):
    a = int(file.readline())
    if a % 2 == 0 and a % 7 != 0 and a > m2:
        m2 = a
    if a % 2 != 0 and a % 7 == 0 and a > m7:
        m7 = a
    if a > m:
        if m % 14 == 0 and m > m14:
            m14 = m
        m = a
    elif a % 14 == 0 and a > m14:
        m14 = a

print(max(m7 * m2, m14 * m))

