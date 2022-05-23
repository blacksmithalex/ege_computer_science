file = open('27991_B.txt')
n = int(file.readline())
a17_0 = 0 # число, которое делится на 17 и четное
a17_1 = 0 #число, которое делится на 17 и нечетное
a_0 = 0 #максимальное четное число, отличное от a17_0
a_1 = 0 #максимальное нечетное число, отлично от a17_1
for _ in range(n):
    r = int(file.readline())
    if r % 2 == 0:
        if r % 17 == 0 and r > a17_0:
            if a17_0 > a_0:
                a_0 = a17_0
            a17_0 = r
        elif r > a_0:
            a_0 = r
    else:
        if r % 17 == 0 and r > a17_1:
            if a17_1 > a_1:
                a_1 = a17_1
            a17_1 = r
        if r > a_1:
            a_1 = r

print(a17_0, a_0)
print(a17_1, a_1)