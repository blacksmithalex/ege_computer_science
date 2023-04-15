def f(x, A):
    l1 = x & 28 != 0
    l2 = x & 45 != 0
    l3 = x & 48 == 0
    l4 = x & A != 0
    return (l1 or l2) <= (l3 <= l4)

for A in range(100):
    flag = True
    for x in range(200):
        if f(x, A) == False:
            flag = False
    if flag:
        print(A)