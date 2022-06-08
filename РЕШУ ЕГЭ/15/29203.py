def f(x, y, A):
    return (3 * x + 7 * y < A) or (x >= y) or (y > 6)

for A in range(100):
    flag = True
    for x in range(150):
        for y in range(150):
            if f(x, y, A) == False:
                flag = False
    if flag == True:
        print(A)