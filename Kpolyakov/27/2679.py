def array_product(a):
    S = 1
    for x in a:
        S *= x
    return S
def max_product(seq):
    negative = []
    for i in range(len(seq)):
        if seq[i] < 0:
            negative.append(i)
    if len(negative) % 2 == 0:
        return array_product(seq)
    p1 = array_product(seq[:negative[-1]])
    p2 = array_product(seq[negative[0] + 1:])
    return max(p1, p2)

file = open('27-19b.txt')
N = int(file.readline())
alls = ''
for _ in range(N):
    alls += str(int(file.readline())) + ' '
file.close()
alls = alls.split('0')
for i in range(len(alls)):
    alls[i] = [int(x) for x in alls[i].split()]

Pmax = 0
for seq in alls:
    Pmax = max(Pmax,max_product(seq))

print(Pmax)
