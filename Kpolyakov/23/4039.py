alls = set()
def f(n, p):
    if p == 13:
        alls.add(n)
    else:
        f(n + 3, p + 1)
        f(n * 2 + 1, p + 1)
f(2, 0)
print(len(alls))

#####
alls = {2}
for _ in range(13):
    cur = set()
    for x in alls:
        cur.add(x + 3)
        cur.add(x * 2 + 1)
    alls = cur
print(len(alls))