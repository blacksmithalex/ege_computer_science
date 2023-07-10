def f(x, A):
    l1 = (x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))
    l2 = (x & 8 == 0) and (x & A != 0) and (x & 58 == 0)
    return l1 <= l2

for A in range(1, 300):
    flag = True
    for x in range(1, 300):
        if f(x, A):
            flag = False
    if flag:
        print(A)
