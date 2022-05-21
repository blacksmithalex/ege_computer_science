file = open('zadanie24_2.txt')
s = file.readline()
file.close()

m, k = 1, 1
for i in range(len(s)):
    if s[i] != s[i - 1]:
        k += 1
        m = max(k, m)
    else:
        k = 1
print(m)