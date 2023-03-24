file = open('17-257.txt')
a = [int(x) for x in file]
file.close()

chet, nech = [], []
for x in a:
    if x % 2 == 0:
        chet.append(x)
    else:
        nech.append(x)

if max(chet) > max(nech):
    print(len(chet), min(chet))
else:
    print(len(nech), min(chet))