file = open('27-B.txt')
N = int(file.readline())
a = [int(x) for x in file]
file.close()

Sr = [None] * 10
Ms, S, Scount = 0, 0, 0

for x in a:
    S += x
    if x % 2 != 0:
        Scount += 1
    if Scount % 10 == 0:
        Ms = S
    else:
        r = Scount % 10
        if Sr[r] is None:
            Sr[r] = S
        else:
            newS = S - Sr[r]
            if newS > Ms:
                Ms = newS
print(Ms)






