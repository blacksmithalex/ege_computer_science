file = open('27-A.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

count = 0
for i in range(N):
    for j in range(i, N):
        subseq = a[i:j + 1]
        product = 1
        for x in subseq:
            product *= x
        if product % 980869 != 0:
            count += 1
print(count)

#A: 203185