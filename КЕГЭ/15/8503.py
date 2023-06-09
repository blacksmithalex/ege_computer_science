def f(x, A):
    l1 = x & 52 != 0
    l2 = x & 36 == 0
    l3 = not (x & A == 0)
    return (l1 and l2) <= l3

for A in range(100):
    flag = True
    for x in range(100):
        if f(x, A) == False:
            flag = False
    if flag:
        print(A)