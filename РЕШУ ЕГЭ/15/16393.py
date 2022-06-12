def f(x, y, A):
    return (2 * x + 3 * y > 30) or (x + y <= A)

for A in range(100):
    flag = True
    for x in range(150):
        for y in range(150):
            if f(x, y, A) == False:
                flag = False
    if flag == True:
        print(A)
        break