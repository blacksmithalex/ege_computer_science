file = open('24.txt')
a = file.readline()
file.close()

inds = [i for i in range(len(a)) if a[i] == 'D']
ml = inds[1]
for i in range(len(inds) - 2):
    l = inds[i + 2] - inds[i] - 1
    ml = max(ml, l)
ml = max(ml, len(a) - inds[-2] - 1)
print(ml)

