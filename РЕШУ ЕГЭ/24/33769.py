file = open('24.txt')
a = file.readline()
file.close()

freq = {}
for i in range(len(a) - 2):
    if a[i] == a[i + 1]:
        freq[a[i + 2]] = freq.get(a[i + 2], 0) + 1
print(freq)


