count, m = 0, 0
file = open('17.txt')
l = [int(i) for i in file]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] - l[j]) % 2 == 0 and (l[i] % 31 == 0 or l[j] % 31 == 0):
            count += 1
            m = max(m, l[i] + l[j])
print(count, m)