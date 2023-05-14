file = open('1234.txt')
n = int(file.readline())
a = [int(x) for x in file]
m = sorted(a, reverse=True)
p = sorted(a)

print(p)
print(m)

psum = 0
msum = 0
for i in range(0, 7500):
    psum += p[i]
    msum += m[i]
for i in range(7500, 10000):
    psum += p[i] * 0.5
    msum += m[i] * 0.5

print(msum, psum)