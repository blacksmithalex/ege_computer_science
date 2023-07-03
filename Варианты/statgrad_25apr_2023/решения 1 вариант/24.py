file = open('24.txt')
a = file.readline()
acopy = list(a)

for i in range(len(a) - 2):
    if {a[i], a[i + 1], a[i + 2]} == set('ABC'):
        acopy[i], acopy[i + 1], acopy[i + 2] = ' ', ' ', ' '
res = ''.join(acopy)
res = res.split()
print(max([len(x) for x in res]))

