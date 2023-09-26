file = open('17_10100.txt')
a = [int(x) for x in file]
file.close()

m13 = 0
for x in a:
    if x % 100 == 13 and x > m13:
        m13 = x

count, sm = 0, 0
for i in range(len(a) - 2):
    elems = [a[i], a[i + 1], a[i + 2]]
    ls = [len(str(x)) for x in elems]
    if ls.count(3) == 2 and sum(elems) <= m13:
        count += 1
        sm = max(sm, a[i] + a[i + 1] + a[i + 2])
print(count, sm)

