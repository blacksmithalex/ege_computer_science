def f(x, y, A):
    return ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))

for A in range(150):
    flag = True
    for x in range(200):
        for y in range(200):
            if f(x, y, A) == False:
                flag = False
    if flag == True:
        print(A)