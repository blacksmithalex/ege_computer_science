def f(N):
    s1 = int(str(N)[0]) + int(str(N)[1])
    s2 = int(str(N)[1]) + int(str(N)[2])
    s3 = int(str(N)[2]) + int(str(N)[3])
    a, b = sorted([s1, s2, s3])[1:]

    if a < b:
        return int(str(a) + str(b))
    else:
        return int(str(a) + str(b))

for N in range(1000, 10000):
    if f(N) == 1515:
        print(N)