def f(x, y, A):
    return (2 * y + 3 * x != 135) or (y > A) or (x > A)

for A in range(300):
    flag = True
    for x in range(300):
        for y in range(300):
            if f(x, y, A) == False:
                flag = False
    if flag:
        print(A)