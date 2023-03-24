from math import ceil
file = open('inf_22_10_20_26.txt')
S = 0 # стоимость покупки
N = int(file.readline())
p = []
for _ in range(N):
    num = int(file.readline())
    if num > 50:
        p.append(num)
    else:
        S += num
file.close()
p = sorted(p)
S += sum(p[:len(p) // 2]) * 0.75 # учли скидку
S += sum(p[len(p) // 2:])
print(ceil(S), p[len(p) // 2 - 1])