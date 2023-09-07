file = open('24_10105.txt')
a = file.readline()
file.close()

inds = [i for i in range(len(a)) if a[i] == 'T']
ml = inds[100]
for i in range(len(inds) - 101):
    l = inds[i + 101] - inds[i] - 1
    ml = max(ml, l)
ml = max(ml, len(a) - inds[-101] - 1)
print(ml)