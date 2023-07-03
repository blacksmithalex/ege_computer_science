from fnmatch import fnmatch as fn

for n in range(4891, 10 ** 10, 4891):
    if fn(str(n),'1?7602*0'):
        print(n)