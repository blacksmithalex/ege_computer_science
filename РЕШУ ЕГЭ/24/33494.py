file = open('24.txt')
a = file.readline()
file.close()

freq = {}
for i in range(len(a) - 1):
    if a[i] == 'E':
        freq[a[i + 1]] = freq.get(a[i + 1], 0) + 1

print(freq)