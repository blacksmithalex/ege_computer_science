def f(x, A):
    return (x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))

for A in range(100):
    flag = True
    for x in range(150):
        if f(x, A) == False:
            flag = False
    if flag == True:
        print(A)