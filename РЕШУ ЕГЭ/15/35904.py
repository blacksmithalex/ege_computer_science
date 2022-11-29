for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not ((A % 40 == 0) and ((780 % x == 0) <= ((A % x != 0) <= (180 % x != 0)))):
            flag = False
    if flag:
        print(A)
        break



