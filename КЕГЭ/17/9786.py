file = open('17_9786.txt')
a = [int(x) for x in file]
file.close()

m25 = 0
for x in a:
    if abs(x) % 100 == 25 and x > m25:
        m25 = x
count, sm = 0, 0
for i in range(len(a) - 2):
    elems = [a[i], a[i + 1], a[i + 2]]
    ls = [len(str(abs(x))) for x in elems]
    if ls.count(4) <= 2 and sum(elems) <= m25:
        count += 1
        sm = max(sm, a[i] + a[i + 1] + a[i + 2])
print(count, sm)