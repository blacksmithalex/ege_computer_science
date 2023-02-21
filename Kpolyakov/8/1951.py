from itertools import permutations
def f(a):
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return False
    return True

count = 0
for a in permutations('МАРТА', 5):
    a = ''.join(a)
    if f(a):
        count += 1
print(count // 2)

