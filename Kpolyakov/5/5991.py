def cmd1(a):
    part = a[-4:]
    part = ''.join([str((int(x) + 1) % 2)  for x in part])
    return a[:-4] + part
def cmd2(a):
    part = a[-5:-1]
    part = ''.join([str((int(x) + 1) % 2) for x in part])
    return a[:-5] + part + a[-1]
def f(n):
    n = bin(n)[2:]
    s = sum([int(x) for x in n])
    if s % 2 == 0:
        n = cmd1(n)
    else:
        n = cmd2(n)
    return int(n, 2)

for n in range(64, 500):
    print(n, f(n))
#n = 94