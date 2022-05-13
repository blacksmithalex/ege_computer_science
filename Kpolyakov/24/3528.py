file = open('24-153.txt')
a = file.readline()
file.close()
indices = [i for i in range(len(a)) if a[i] == 'D']
diff = [indices[i + 1] - indices[i] + 1 for i in range(len(indices) - 1) if indices[i + 1] - indices[i] + 1 > 2]
print(min(diff))