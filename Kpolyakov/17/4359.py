def isFit(n):
    return sum([int(x) for x in str(n)]) % 3 == 0

count, nmax = 0, 0
file = open('17-7.txt')
a = [int(x) for x in file]
file.close()

for x in a:
    if isFit(x):
        count += 1
        if x > nmax:
            nmax = x
print(count, nmax)