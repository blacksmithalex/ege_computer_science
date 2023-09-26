file = open('17_7596.txt')
a = [int(x) for x in file]
file.close()

min5 = 100000
for x in a:
    if x % 10 == 5 and x < min5:
        min5 = x

count, sm = 0, 200000
for i in range(len(a) - 1):
    elems = [a[i], a[i + 1]]
    ls = [len(str(abs(x))) for x in elems]
    if ls.count(3) == 1 and sum(elems) % min5 == 0:
        count += 1
        sm = min(sm, a[i] + a[i + 1])
print(count, sm)
