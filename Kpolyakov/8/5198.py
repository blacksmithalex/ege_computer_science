def f(a):
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return False
    return True

alp = sorted('СТЕПУХА')
count = 1
nums = 0
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                a = a1 + a2 + a3 + a4
                if count > 1000 and f(a):
                    nums += 1
                count += 1
print(nums)