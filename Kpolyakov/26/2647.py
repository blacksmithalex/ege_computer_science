file = open('26-j5.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

out = 0
for i in range(1, N - 1):
    mean = sorted([a[i - 1], a[i], a[i +1]])[1]
    if mean < a[i]:
        out += a[i] - mean
print(out)





